PGDMP         /                 {            delivery_sys    14.5    14.5 ?    ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    115028    delivery_sys    DATABASE     p   CREATE DATABASE delivery_sys WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE delivery_sys;
                postgres    false                       1255    118847    add_bc_to_metro()    FUNCTION     ?  CREATE FUNCTION public.add_bc_to_metro() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
    DECLARE
        bc_id INT;
        bc_metro_id INT;
    BEGIN
        bc_id := NEW.bc_id;
        bc_metro_id := NEW.bc_metro_id;
        EXECUTE format('UPDATE public.Metro_station SET metro_station_bc_id = metro_station_bc_id || %s WHERE metro_station_id = %s;', bc_id, bc_metro_id);
        RETURN NEW;
    END;
    $$;
 (   DROP FUNCTION public.add_bc_to_metro();
       public          postgres    false                        1255    118845    add_client_to_bc()    FUNCTION     ?  CREATE FUNCTION public.add_client_to_bc() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
    DECLARE
        bc_id INT;
        client_id INT;
    BEGIN
        bc_id := NEW.client_bc_id;
        client_id := NEW.client_id;
        EXECUTE format('UPDATE public.Business_center SET bc_clients_id = bc_clients_id || %s WHERE bc_id = %s;', client_id, bc_id);
        INSERT INTO Document_delivery_sheet (DDS_client_id) VALUES (client_id);
        IF (SELECT 1 FROM Document_delivery_sheet WHERE DDS_client_id = client_id) IS NOT NULL THEN
            RETURN NEW;
        ELSE
            RAISE EXCEPTION 'Не удалось создать клиента!';
        END IF;
    END;
    $$;
 )   DROP FUNCTION public.add_client_to_bc();
       public          postgres    false            ?            1255    118842    add_contacts_to_company()    FUNCTION     ?  CREATE FUNCTION public.add_contacts_to_company() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
    DECLARE
        contact_id INTEGER;
        com_id INTEGER;
    BEGIN
        contact_id := NEW.contact_person_id;
        com_id := NEW.contact_person_company_id;
        EXECUTE format('UPDATE public.Company SET company_contacts_id = company_contacts_id || %s WHERE company_id = %s;', contact_id, com_id);
        RETURN NEW;
    END;
    $$;
 0   DROP FUNCTION public.add_contacts_to_company();
       public          postgres    false                       1255    118849    add_date_to_dds(integer)    FUNCTION     ?  CREATE FUNCTION public.add_date_to_dds(client_id integer) RETURNS void
    LANGUAGE plpgsql
    AS $$
    DECLARE
        date DATE;
        mas DATE[];
    BEGIN
        date := now();
        mas := (SELECT dds_dates FROM Document_delivery_sheet WHERE DDS_client_id = client_id);
        mas := mas || date;
        EXECUTE format('UPDATE public.Document_delivery_sheet SET dds_dates = %L WHERE dds_client_id = %s;', mas, client_id);
    END;
    $$;
 9   DROP FUNCTION public.add_date_to_dds(client_id integer);
       public          postgres    false            ?           0    0 +   FUNCTION add_date_to_dds(client_id integer)    ACL     L   GRANT ALL ON FUNCTION public.add_date_to_dds(client_id integer) TO courier;
          public          postgres    false    258            ?            1255    118833    change_task_cour()    FUNCTION     C  CREATE FUNCTION public.change_task_cour() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
    BEGIN
        --ТОЛЬКО АДМИН МОЖЕТ МЕНЯТЬ ВЫПОЛНЕННОЕ ЗАДАНИЕ
        IF (OLD.task_condition = '+' AND (SELECT user_role FROM user_data WHERE user_login = current_user) <> 3) THEN
            RAISE EXCEPTION 'Выполненное задание нельзя изменить!';

        --КУРЬЕР НЕ МОЖЕТ ИЗМЕНИТЬ СОСТОЯНИЕ ЧУЖОГО ЗАДАНИЯ
        ELSIF OLD.task_user_id <> (SELECT user_id FROM user_data WHERE user_login = current_user) THEN
            RAISE EXCEPTION 'Чужое задание нельзя изменить';
        ELSE
            NEW.task_execution_date = now();
            RETURN NEW;
        END IF;
    END
    $$;
 )   DROP FUNCTION public.change_task_cour();
       public          postgres    false                       1255    118832    change_task_man()    FUNCTION     ?  CREATE FUNCTION public.change_task_man() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
    BEGIN
        --ТОЛЬКО АДМИН МОЖЕТ МЕНЯТЬ ВЫПОЛНЕННОЕ ЗАДАНИЕ
        IF (OLD.task_condition = '+' AND (SELECT user_role FROM user_data WHERE user_login = current_user) <> 3) THEN
            RAISE EXCEPTION 'Выполненное задание нельзя изменить!';
        ELSE RETURN NEW;
        END IF;
    END
    $$;
 (   DROP FUNCTION public.change_task_man();
       public          postgres    false            ?            1255    118836    clear_tasks() 	   PROCEDURE     ?   CREATE PROCEDURE public.clear_tasks()
    LANGUAGE plpgsql
    AS $$
    BEGIN
        DELETE FROM Task WHERE(now() - task_execution_date >= INTERVAL '6 MONTH');
    END;
    $$;
 %   DROP PROCEDURE public.clear_tasks();
       public          postgres    false            ?           0    0    PROCEDURE clear_tasks()    ACL     8   GRANT ALL ON PROCEDURE public.clear_tasks() TO manager;
          public          postgres    false    250                       1255    118858    completed_task(integer) 	   PROCEDURE     	  CREATE PROCEDURE public.completed_task(IN task_id integer)
    LANGUAGE plpgsql
    AS $$
    DECLARE
        s CHAR;
    BEGIN
        s := '+';
        EXECUTE format('UPDATE Task SET task_condition = %L WHERE task_id = %L;', s, task_id);
    END;
    $$;
 :   DROP PROCEDURE public.completed_task(IN task_id integer);
       public          postgres    false            ?           0    0 ,   PROCEDURE completed_task(IN task_id integer)    ACL     M   GRANT ALL ON PROCEDURE public.completed_task(IN task_id integer) TO courier;
          public          postgres    false    259                       1255    118851 C   create_bc(character varying, character varying, character, integer) 	   PROCEDURE     t  CREATE PROCEDURE public.create_bc(IN bc_name character varying, IN bc_address character varying, IN passes character, IN metro_id integer)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        EXECUTE format('INSERT INTO public.Business_center (BC_name, BC_address,BC_passes, BC_metro_id) VALUES (%L, %L, %L, %L);', bc_name, bc_address, passes, metro_id);
    END;
    $$;
 ?   DROP PROCEDURE public.create_bc(IN bc_name character varying, IN bc_address character varying, IN passes character, IN metro_id integer);
       public          postgres    false            ?           0    0 |   PROCEDURE create_bc(IN bc_name character varying, IN bc_address character varying, IN passes character, IN metro_id integer)    ACL     ?   GRANT ALL ON PROCEDURE public.create_bc(IN bc_name character varying, IN bc_address character varying, IN passes character, IN metro_id integer) TO manager;
          public          postgres    false    263            ?            1255    118840    create_client_from_company()    FUNCTION     ~  CREATE FUNCTION public.create_client_from_company() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
    DECLARE
        type varchar(10);
        name varchar(50);
        bc_id INTEGER;
    BEGIN
        IF OLD.company_contacts_id IS NULL AND array_length(NEW.company_contacts_id, 1) > 0 THEN
            type := 2;
            name := NEW.company_name;
            bc_id := NEW.company_bc_id;
            EXECUTE format('INSERT INTO public.Client (client_type, client_name, client_bc_id) VALUES (%s, ''%s'', ''%s'');', type, name, bc_id);
            RETURN NEW;
        ELSE RETURN NULL;
        END IF;
    END;
    $$;
 3   DROP FUNCTION public.create_client_from_company();
       public          postgres    false            ?            1255    118838    create_client_from_ie()    FUNCTION     ?  CREATE FUNCTION public.create_client_from_ie() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
    DECLARE
        type varchar(10);
        name varchar(50);
        bc_id INTEGER;
    BEGIN
        type := 1;
        name := NEW.ie_lastname;
        bc_id := NEW.ie_bc_id;
        EXECUTE format('INSERT INTO public.Client (client_type, client_name, client_bc_id) VALUES (%s, ''%s'', ''%s'');', type, name, bc_id);
        RETURN NEW;
    END;
    $$;
 .   DROP FUNCTION public.create_client_from_ie();
       public          postgres    false                       1255    118854 o   create_company(character varying, character varying, character, integer, character, character varying, integer) 	   PROCEDURE     ?  CREATE PROCEDURE public.create_company(IN name character varying, IN office_num character varying, IN call_ahead character, IN contract_id integer, IN contract_received character, IN description character varying, IN bc_id integer)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        EXECUTE format('INSERT INTO public.Company ' ||
                       '(company_name, company_office_num, company_call_ahead, company_contract_id, ' ||
                       'company_contract_received, company_description, company_bc_id) ' ||
                       'VALUES (%L, %L, %L, %L, %L, %L, %L);',
            name, office_num, call_ahead, contract_id,contract_received, description, bc_id);
    END;
    $$;
 ?   DROP PROCEDURE public.create_company(IN name character varying, IN office_num character varying, IN call_ahead character, IN contract_id integer, IN contract_received character, IN description character varying, IN bc_id integer);
       public          postgres    false            ?           0    0 ?   PROCEDURE create_company(IN name character varying, IN office_num character varying, IN call_ahead character, IN contract_id integer, IN contract_received character, IN description character varying, IN bc_id integer)    ACL     ?   GRANT ALL ON PROCEDURE public.create_company(IN name character varying, IN office_num character varying, IN call_ahead character, IN contract_id integer, IN contract_received character, IN description character varying, IN bc_id integer) TO manager;
          public          postgres    false    268            	           1255    118855 M   create_contact_person(character varying, character varying, numeric, integer) 	   PROCEDURE       CREATE PROCEDURE public.create_contact_person(IN fname character varying, IN lname character varying, IN phone numeric, IN company_id integer)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        EXECUTE format('INSERT INTO public.Contact_person ' ||
                       '(contact_person_firstname, contact_person_lastname, ' ||
                       'contact_person_phonenum, contact_person_company_id) ' ||
                       'VALUES (%L, %L, %L, %L);',
            fname, lname, phone, company_id);
    END;
    $$;
 ?   DROP PROCEDURE public.create_contact_person(IN fname character varying, IN lname character varying, IN phone numeric, IN company_id integer);
       public          postgres    false            ?           0    0 ?   PROCEDURE create_contact_person(IN fname character varying, IN lname character varying, IN phone numeric, IN company_id integer)    ACL     ?   GRANT ALL ON PROCEDURE public.create_contact_person(IN fname character varying, IN lname character varying, IN phone numeric, IN company_id integer) TO manager;
          public          postgres    false    265                       1255    118852 !   create_contract(numeric, integer) 	   PROCEDURE     	  CREATE PROCEDURE public.create_contract(IN num numeric, IN service_id integer)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        EXECUTE format('INSERT INTO public.Contract (contract_num, contract_service_id) VALUES (%L, %L);',num, service_id);
    END;
    $$;
 N   DROP PROCEDURE public.create_contract(IN num numeric, IN service_id integer);
       public          postgres    false            ?           0    0 @   PROCEDURE create_contract(IN num numeric, IN service_id integer)    ACL     a   GRANT ALL ON PROCEDURE public.create_contract(IN num numeric, IN service_id integer) TO manager;
          public          postgres    false    260                       1255    118853 ?   create_ie(character varying, character varying, numeric, integer, character varying, character, character, character varying, integer) 	   PROCEDURE       CREATE PROCEDURE public.create_ie(IN fname character varying, IN lname character varying, IN phone numeric, IN contract_id integer, IN office_num character varying, IN call_ahead character, IN contract_received character, IN description character varying, IN bc_id integer)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        EXECUTE format('INSERT INTO public.Individual_entrepreneur ' ||
                       '(ie_firstname, ie_lastname, ie_phone, ie_contract_id, ' ||
                       'ie_office_num, ie_description, ie_call_ahead, ie_contract_received, IE_BC_id) ' ||
                       'VALUES (%L, %L, %L, %L, %L, %L, %L, %L, %L);',
            fname, lname, phone, contract_id,office_num, description, call_ahead, contract_received, bc_id);
    END;
    $$;
   DROP PROCEDURE public.create_ie(IN fname character varying, IN lname character varying, IN phone numeric, IN contract_id integer, IN office_num character varying, IN call_ahead character, IN contract_received character, IN description character varying, IN bc_id integer);
       public          postgres    false            ?           0    0   PROCEDURE create_ie(IN fname character varying, IN lname character varying, IN phone numeric, IN contract_id integer, IN office_num character varying, IN call_ahead character, IN contract_received character, IN description character varying, IN bc_id integer)    ACL     $  GRANT ALL ON PROCEDURE public.create_ie(IN fname character varying, IN lname character varying, IN phone numeric, IN contract_id integer, IN office_num character varying, IN call_ahead character, IN contract_received character, IN description character varying, IN bc_id integer) TO manager;
          public          postgres    false    269            ?            1255    118850    create_metro(character varying) 	   PROCEDURE     ?   CREATE PROCEDURE public.create_metro(IN station_name character varying)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        EXECUTE format('INSERT INTO public.Metro_station (metro_station_name) VALUES (%L);', station_name);
    END;
    $$;
 G   DROP PROCEDURE public.create_metro(IN station_name character varying);
       public          postgres    false            ?           0    0 9   PROCEDURE create_metro(IN station_name character varying)    ACL     Z   GRANT ALL ON PROCEDURE public.create_metro(IN station_name character varying) TO manager;
          public          postgres    false    254                       1255    121165 *   create_service(character varying, integer) 	   PROCEDURE     T  CREATE PROCEDURE public.create_service(IN name character varying, IN price integer)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        EXECUTE format('INSERT INTO public.Service ' ||
                       '(service_name, service_price) ' ||
                       'VALUES (%L, %L);',
            name, price::money);
    END;
    $$;
 S   DROP PROCEDURE public.create_service(IN name character varying, IN price integer);
       public          postgres    false            
           1255    118857 (   create_service(character varying, money) 	   PROCEDURE     K  CREATE PROCEDURE public.create_service(IN name character varying, IN price money)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        EXECUTE format('INSERT INTO public.Service ' ||
                       '(service_name, service_price) ' ||
                       'VALUES (%L, %L);',
            name, price);
    END;
    $$;
 Q   DROP PROCEDURE public.create_service(IN name character varying, IN price money);
       public          postgres    false            ?           0    0 C   PROCEDURE create_service(IN name character varying, IN price money)    ACL     d   GRANT ALL ON PROCEDURE public.create_service(IN name character varying, IN price money) TO manager;
          public          postgres    false    266                       1255    118856 %   create_task(integer[], date, integer) 	   PROCEDURE     ?  CREATE PROCEDURE public.create_task(IN metro_id integer[], IN close_date date, IN user_id integer)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        EXECUTE format('INSERT INTO public.Task ' ||
                       '(task_metro_id, task_close_date, ' ||
                       'task_user_id) ' ||
                       'VALUES (%L, %L, %L);',
            metro_id, close_date,user_id);
    END;
    $$;
 b   DROP PROCEDURE public.create_task(IN metro_id integer[], IN close_date date, IN user_id integer);
       public          postgres    false            ?           0    0 T   PROCEDURE create_task(IN metro_id integer[], IN close_date date, IN user_id integer)    ACL     u   GRANT ALL ON PROCEDURE public.create_task(IN metro_id integer[], IN close_date date, IN user_id integer) TO manager;
          public          postgres    false    261            ?            1255    118844 :   create_user(character varying, integer, character varying) 	   PROCEDURE     ?  CREATE PROCEDURE public.create_user(IN login character varying, IN id_role integer, IN pass character varying)
    LANGUAGE plpgsql
    AS $$
    DECLARE
        role TEXT;
    BEGIN
        role := (SELECT role_name FROM Role WHERE role_id = id_role);
        BEGIN
        EXECUTE format('CREATE USER %s IN ROLE %s ENCRYPTED PASSWORD ''%s'';', login, role, pass);
        EXECUTE format('INSERT INTO public.User_data (user_login, user_role) VALUES (%L, %L);', login, id_role);
        IF (SELECT 1 FROM pg_roles WHERE rolname = login) IS NOT NULL THEN
            COMMIT;
        ELSE
            ROLLBACK;
        END IF;
        END;
    END;
    $$;
 n   DROP PROCEDURE public.create_user(IN login character varying, IN id_role integer, IN pass character varying);
       public          postgres    false            ?           0    0 `   PROCEDURE create_user(IN login character varying, IN id_role integer, IN pass character varying)    ACL        GRANT ALL ON PROCEDURE public.create_user(IN login character varying, IN id_role integer, IN pass character varying) TO admin;
          public          postgres    false    255            ?            1255    118837    delete_user(character varying) 	   PROCEDURE     ?  CREATE PROCEDURE public.delete_user(IN login character varying)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        BEGIN
        EXECUTE format('DELETE FROM User_data WHERE user_login = %L;', login);
        EXECUTE format('DROP USER IF EXISTS %s;', login);
        IF (SELECT 1 FROM pg_roles WHERE rolname= login) IS NULL THEN
            COMMIT;
        ELSE
            ROLLBACK;
        END IF;
        END;
    END;
    $$;
 ?   DROP PROCEDURE public.delete_user(IN login character varying);
       public          postgres    false            ?           0    0 1   PROCEDURE delete_user(IN login character varying)    ACL     P   GRANT ALL ON PROCEDURE public.delete_user(IN login character varying) TO admin;
          public          postgres    false    248                       1255    118859    ready_metro(integer) 	   PROCEDURE     ?   CREATE PROCEDURE public.ready_metro(IN metro_id integer)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        EXECUTE format('UPDATE Metro_station SET metro_station_doc_condition = ''+'' WHERE metro_station_id = %L;', metro_id);
    END;
    $$;
 8   DROP PROCEDURE public.ready_metro(IN metro_id integer);
       public          postgres    false            ?           0    0 *   PROCEDURE ready_metro(IN metro_id integer)    ACL     K   GRANT ALL ON PROCEDURE public.ready_metro(IN metro_id integer) TO manager;
          public          postgres    false    267            ?            1259    125722    task    TABLE     ?  CREATE TABLE public.task (
    task_id integer NOT NULL,
    task_condition "char" DEFAULT '-'::"char" NOT NULL,
    task_metro_id integer[] NOT NULL,
    task_start_date date DEFAULT now() NOT NULL,
    task_close_date date NOT NULL,
    task_execution_date date,
    task_user_id integer NOT NULL,
    CONSTRAINT task_task_condition_check CHECK (((task_condition = '-'::"char") OR (task_condition = '+'::"char")))
);
    DROP TABLE public.task;
       public         heap    postgres    false            ?           0    0 
   TABLE task    ACL     ?   GRANT ALL ON TABLE public.task TO admin;
GRANT SELECT,DELETE ON TABLE public.task TO manager;
GRANT SELECT ON TABLE public.task TO courier;
          public          postgres    false    234            ?           0    0    COLUMN task.task_condition    ACL     >   GRANT UPDATE(task_condition) ON TABLE public.task TO courier;
          public          postgres    false    234    3553            ?           0    0    COLUMN task.task_metro_id    ACL     S   GRANT INSERT(task_metro_id),UPDATE(task_metro_id) ON TABLE public.task TO manager;
          public          postgres    false    234    3553            ?           0    0    COLUMN task.task_close_date    ACL     W   GRANT INSERT(task_close_date),UPDATE(task_close_date) ON TABLE public.task TO manager;
          public          postgres    false    234    3553            ?           0    0    COLUMN task.task_user_id    ACL     Q   GRANT INSERT(task_user_id),UPDATE(task_user_id) ON TABLE public.task TO manager;
          public          postgres    false    234    3553            ?            1259    125816    bad_task    VIEW     p   CREATE VIEW public.bad_task AS
 SELECT task.task_id
   FROM public.task
  WHERE (task.task_close_date < now());
    DROP VIEW public.bad_task;
       public          postgres    false    234    234            ?            1259    125640    business_center    TABLE     ?  CREATE TABLE public.business_center (
    bc_id integer NOT NULL,
    bc_name character varying(30) NOT NULL,
    bc_address character varying(50) NOT NULL,
    bc_passes "char" DEFAULT '-'::"char" NOT NULL,
    bc_clients_id integer[],
    bc_metro_id integer NOT NULL,
    CONSTRAINT business_center_bc_passes_check CHECK (((bc_passes = '-'::"char") OR (bc_passes = '+'::"char")))
);
 #   DROP TABLE public.business_center;
       public         heap    postgres    false            ?           0    0    TABLE business_center    ACL     ?   GRANT ALL ON TABLE public.business_center TO admin;
GRANT SELECT,INSERT,UPDATE ON TABLE public.business_center TO manager;
GRANT SELECT ON TABLE public.business_center TO courier;
          public          postgres    false    220            ?            1259    125639    business_center_bc_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.business_center_bc_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.business_center_bc_id_seq;
       public          postgres    false    220            ?           0    0    business_center_bc_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.business_center_bc_id_seq OWNED BY public.business_center.bc_id;
          public          postgres    false    219            ?           0    0 "   SEQUENCE business_center_bc_id_seq    ACL     ?   GRANT USAGE ON SEQUENCE public.business_center_bc_id_seq TO manager;
GRANT USAGE ON SEQUENCE public.business_center_bc_id_seq TO admin;
          public          postgres    false    219            ?            1259    125609    client    TABLE     ?   CREATE TABLE public.client (
    client_id integer NOT NULL,
    client_type smallint NOT NULL,
    client_name character varying(50) NOT NULL,
    client_bc_id integer NOT NULL
);
    DROP TABLE public.client;
       public         heap    postgres    false            ?           0    0    TABLE client    ACL     ?   GRANT ALL ON TABLE public.client TO admin;
GRANT SELECT,INSERT,UPDATE ON TABLE public.client TO manager;
GRANT SELECT ON TABLE public.client TO courier;
          public          postgres    false    214            ?            1259    125608    client_client_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.client_client_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.client_client_id_seq;
       public          postgres    false    214            ?           0    0    client_client_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.client_client_id_seq OWNED BY public.client.client_id;
          public          postgres    false    213            ?           0    0    SEQUENCE client_client_id_seq    ACL     ~   GRANT USAGE ON SEQUENCE public.client_client_id_seq TO manager;
GRANT USAGE ON SEQUENCE public.client_client_id_seq TO admin;
          public          postgres    false    213            ?            1259    125616    client_type    TABLE     t   CREATE TABLE public.client_type (
    client_type_id integer NOT NULL,
    client_type_name character varying(8)
);
    DROP TABLE public.client_type;
       public         heap    postgres    false            ?           0    0    TABLE client_type    ACL     ?   GRANT ALL ON TABLE public.client_type TO admin;
GRANT SELECT ON TABLE public.client_type TO courier;
GRANT SELECT ON TABLE public.client_type TO manager;
          public          postgres    false    216            ?            1259    125615    client_type_client_type_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.client_type_client_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.client_type_client_type_id_seq;
       public          postgres    false    216            ?           0    0    client_type_client_type_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.client_type_client_type_id_seq OWNED BY public.client_type.client_type_id;
          public          postgres    false    215            ?           0    0 '   SEQUENCE client_type_client_type_id_seq    ACL     ?   GRANT USAGE ON SEQUENCE public.client_type_client_type_id_seq TO manager;
GRANT USAGE ON SEQUENCE public.client_type_client_type_id_seq TO admin;
          public          postgres    false    215            ?            1259    125705    company    TABLE     ?  CREATE TABLE public.company (
    company_id integer NOT NULL,
    company_name character varying(30) NOT NULL,
    company_office_num character varying(10) NOT NULL,
    company_contacts_id integer[],
    company_call_ahead "char" DEFAULT '-'::"char" NOT NULL,
    company_contract_id integer NOT NULL,
    company_contract_received "char" DEFAULT '-'::"char" NOT NULL,
    company_description character varying(100),
    company_bc_id integer NOT NULL,
    CONSTRAINT company_company_call_ahead_check CHECK (((company_call_ahead = '-'::"char") OR (company_call_ahead = '+'::"char"))),
    CONSTRAINT company_company_contract_received_check CHECK (((company_contract_received = '-'::"char") OR (company_contract_received = '+'::"char")))
);
    DROP TABLE public.company;
       public         heap    postgres    false            ?           0    0    TABLE company    ACL     ?   GRANT ALL ON TABLE public.company TO admin;
GRANT SELECT,INSERT,UPDATE ON TABLE public.company TO manager;
GRANT SELECT ON TABLE public.company TO courier;
          public          postgres    false    232            ?            1259    125704    company_company_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.company_company_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.company_company_id_seq;
       public          postgres    false    232            ?           0    0    company_company_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.company_company_id_seq OWNED BY public.company.company_id;
          public          postgres    false    231            ?           0    0    SEQUENCE company_company_id_seq    ACL     ?   GRANT USAGE ON SEQUENCE public.company_company_id_seq TO manager;
GRANT USAGE ON SEQUENCE public.company_company_id_seq TO admin;
          public          postgres    false    231            ?            1259    125655    contact_person    TABLE     ,  CREATE TABLE public.contact_person (
    contact_person_id integer NOT NULL,
    contact_person_firstname character varying(30) NOT NULL,
    contact_person_lastname character varying(30) NOT NULL,
    contact_person_phonenum numeric(11,0) NOT NULL,
    contact_person_company_id integer NOT NULL
);
 "   DROP TABLE public.contact_person;
       public         heap    postgres    false            ?           0    0    TABLE contact_person    ACL     ?   GRANT ALL ON TABLE public.contact_person TO admin;
GRANT SELECT,INSERT,UPDATE ON TABLE public.contact_person TO manager;
GRANT SELECT ON TABLE public.contact_person TO courier;
          public          postgres    false    222            ?            1259    125654 $   contact_person_contact_person_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.contact_person_contact_person_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public.contact_person_contact_person_id_seq;
       public          postgres    false    222            ?           0    0 $   contact_person_contact_person_id_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public.contact_person_contact_person_id_seq OWNED BY public.contact_person.contact_person_id;
          public          postgres    false    221            ?           0    0 -   SEQUENCE contact_person_contact_person_id_seq    ACL     ?   GRANT USAGE ON SEQUENCE public.contact_person_contact_person_id_seq TO manager;
GRANT USAGE ON SEQUENCE public.contact_person_contact_person_id_seq TO admin;
          public          postgres    false    221            ?            1259    125662    contract    TABLE     ?   CREATE TABLE public.contract (
    contract_id integer NOT NULL,
    contract_num numeric(10,0) NOT NULL,
    contract_service_id smallint
);
    DROP TABLE public.contract;
       public         heap    postgres    false            ?           0    0    TABLE contract    ACL     ?   GRANT ALL ON TABLE public.contract TO admin;
GRANT SELECT,INSERT ON TABLE public.contract TO manager;
GRANT SELECT ON TABLE public.contract TO courier;
          public          postgres    false    224            ?            1259    125661    contract_contract_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.contract_contract_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.contract_contract_id_seq;
       public          postgres    false    224            ?           0    0    contract_contract_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.contract_contract_id_seq OWNED BY public.contract.contract_id;
          public          postgres    false    223            ?           0    0 !   SEQUENCE contract_contract_id_seq    ACL     ?   GRANT USAGE ON SEQUENCE public.contract_contract_id_seq TO manager;
GRANT USAGE ON SEQUENCE public.contract_contract_id_seq TO admin;
          public          postgres    false    223            ?            1259    125671    document_delivery_sheet    TABLE     ?   CREATE TABLE public.document_delivery_sheet (
    dds_id integer NOT NULL,
    dds_dates date[],
    dds_client_id integer NOT NULL
);
 +   DROP TABLE public.document_delivery_sheet;
       public         heap    postgres    false            ?           0    0    TABLE document_delivery_sheet    ACL     ?   GRANT ALL ON TABLE public.document_delivery_sheet TO admin;
GRANT SELECT,INSERT ON TABLE public.document_delivery_sheet TO manager;
GRANT SELECT ON TABLE public.document_delivery_sheet TO courier;
          public          postgres    false    226            ?           0    0 (   COLUMN document_delivery_sheet.dds_dates    ACL     L   GRANT UPDATE(dds_dates) ON TABLE public.document_delivery_sheet TO courier;
          public          postgres    false    226    3576            ?            1259    125670 "   document_delivery_sheet_dds_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.document_delivery_sheet_dds_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public.document_delivery_sheet_dds_id_seq;
       public          postgres    false    226            ?           0    0 "   document_delivery_sheet_dds_id_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE public.document_delivery_sheet_dds_id_seq OWNED BY public.document_delivery_sheet.dds_id;
          public          postgres    false    225            ?           0    0 +   SEQUENCE document_delivery_sheet_dds_id_seq    ACL     ?   GRANT USAGE ON SEQUENCE public.document_delivery_sheet_dds_id_seq TO manager;
GRANT USAGE ON SEQUENCE public.document_delivery_sheet_dds_id_seq TO admin;
          public          postgres    false    225            ?            1259    125680    individual_entrepreneur    TABLE     ?  CREATE TABLE public.individual_entrepreneur (
    ie_id integer NOT NULL,
    ie_firstname character varying(30) NOT NULL,
    ie_lastname character varying(30) NOT NULL,
    ie_phone numeric(11,0) NOT NULL,
    ie_contract_id integer NOT NULL,
    ie_office_num character varying(10),
    ie_call_ahead "char" DEFAULT '-'::"char",
    ie_contract_received "char" DEFAULT '-'::"char",
    ie_description character varying(100),
    ie_bc_id integer NOT NULL,
    CONSTRAINT individual_entrepreneur_ie_call_ahead_check CHECK (((ie_call_ahead = '-'::"char") OR (ie_call_ahead = '+'::"char"))),
    CONSTRAINT individual_entrepreneur_ie_contract_received_check CHECK (((ie_contract_received = '-'::"char") OR (ie_contract_received = '+'::"char")))
);
 +   DROP TABLE public.individual_entrepreneur;
       public         heap    postgres    false            ?           0    0    TABLE individual_entrepreneur    ACL     ?   GRANT ALL ON TABLE public.individual_entrepreneur TO admin;
GRANT SELECT,INSERT,UPDATE ON TABLE public.individual_entrepreneur TO manager;
GRANT SELECT ON TABLE public.individual_entrepreneur TO courier;
          public          postgres    false    228            ?            1259    125679 !   individual_entrepreneur_ie_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.individual_entrepreneur_ie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.individual_entrepreneur_ie_id_seq;
       public          postgres    false    228            ?           0    0 !   individual_entrepreneur_ie_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.individual_entrepreneur_ie_id_seq OWNED BY public.individual_entrepreneur.ie_id;
          public          postgres    false    227            ?           0    0 *   SEQUENCE individual_entrepreneur_ie_id_seq    ACL     ?   GRANT USAGE ON SEQUENCE public.individual_entrepreneur_ie_id_seq TO manager;
GRANT USAGE ON SEQUENCE public.individual_entrepreneur_ie_id_seq TO admin;
          public          postgres    false    227            ?            1259    125625    metro_station    TABLE     ?  CREATE TABLE public.metro_station (
    metro_station_id integer NOT NULL,
    metro_station_name character varying(30) NOT NULL,
    metro_station_bc_id integer[],
    metro_station_doc_condition "char" DEFAULT '-'::"char" NOT NULL,
    CONSTRAINT metro_station_metro_station_doc_condition_check CHECK (((metro_station_doc_condition = '-'::"char") OR (metro_station_doc_condition = '+'::"char")))
);
 !   DROP TABLE public.metro_station;
       public         heap    postgres    false            ?           0    0    TABLE metro_station    ACL     ?   GRANT ALL ON TABLE public.metro_station TO admin;
GRANT SELECT,INSERT,UPDATE ON TABLE public.metro_station TO manager;
GRANT SELECT ON TABLE public.metro_station TO courier;
          public          postgres    false    218            ?            1259    125624 "   metro_station_metro_station_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.metro_station_metro_station_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public.metro_station_metro_station_id_seq;
       public          postgres    false    218                        0    0 "   metro_station_metro_station_id_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE public.metro_station_metro_station_id_seq OWNED BY public.metro_station.metro_station_id;
          public          postgres    false    217                       0    0 +   SEQUENCE metro_station_metro_station_id_seq    ACL     ?   GRANT USAGE ON SEQUENCE public.metro_station_metro_station_id_seq TO manager;
GRANT USAGE ON SEQUENCE public.metro_station_metro_station_id_seq TO admin;
          public          postgres    false    217            ?            1259    125812    ready_metro    VIEW       CREATE VIEW public.ready_metro AS
 SELECT metro_station.metro_station_id,
    metro_station.metro_station_name
   FROM public.metro_station
  WHERE ((metro_station.metro_station_doc_condition = '+'::"char") AND (array_length(metro_station.metro_station_bc_id, 1) IS NOT NULL));
    DROP VIEW public.ready_metro;
       public          postgres    false    218    218    218    218            ?            1259    125600    role    TABLE     h   CREATE TABLE public.role (
    role_id integer NOT NULL,
    role_name character varying(7) NOT NULL
);
    DROP TABLE public.role;
       public         heap    postgres    false                       0    0 
   TABLE role    ACL     )   GRANT ALL ON TABLE public.role TO admin;
          public          postgres    false    212            ?            1259    125599    role_role_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.role_role_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.role_role_id_seq;
       public          postgres    false    212                       0    0    role_role_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.role_role_id_seq OWNED BY public.role.role_id;
          public          postgres    false    211                       0    0    SEQUENCE role_role_id_seq    ACL     v   GRANT USAGE ON SEQUENCE public.role_role_id_seq TO manager;
GRANT USAGE ON SEQUENCE public.role_role_id_seq TO admin;
          public          postgres    false    211            ?            1259    125590    service    TABLE     ?   CREATE TABLE public.service (
    service_id integer NOT NULL,
    service_name character varying(50) NOT NULL,
    service_price money NOT NULL,
    CONSTRAINT service_service_price_check CHECK ((service_price > (0)::money))
);
    DROP TABLE public.service;
       public         heap    postgres    false                       0    0    TABLE service    ACL     ?   GRANT ALL ON TABLE public.service TO admin;
GRANT SELECT,INSERT ON TABLE public.service TO manager;
GRANT SELECT ON TABLE public.service TO courier;
          public          postgres    false    210            ?            1259    125589    service_service_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.service_service_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.service_service_id_seq;
       public          postgres    false    210                       0    0    service_service_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.service_service_id_seq OWNED BY public.service.service_id;
          public          postgres    false    209                       0    0    SEQUENCE service_service_id_seq    ACL     ?   GRANT USAGE ON SEQUENCE public.service_service_id_seq TO manager;
GRANT USAGE ON SEQUENCE public.service_service_id_seq TO admin;
          public          postgres    false    209            ?            1259    125721    task_task_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.task_task_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.task_task_id_seq;
       public          postgres    false    234                       0    0    task_task_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.task_task_id_seq OWNED BY public.task.task_id;
          public          postgres    false    233            	           0    0    SEQUENCE task_task_id_seq    ACL     v   GRANT USAGE ON SEQUENCE public.task_task_id_seq TO manager;
GRANT USAGE ON SEQUENCE public.task_task_id_seq TO admin;
          public          postgres    false    233            ?            1259    125695 	   user_data    TABLE     ?   CREATE TABLE public.user_data (
    user_id integer NOT NULL,
    user_login character varying(20),
    user_role smallint NOT NULL,
    CONSTRAINT user_data_user_login_check CHECK (((user_login)::text <> 'postgres'::text))
);
    DROP TABLE public.user_data;
       public         heap    postgres    false            
           0    0    TABLE user_data    ACL     ?   GRANT ALL ON TABLE public.user_data TO admin;
GRANT SELECT ON TABLE public.user_data TO courier;
GRANT SELECT ON TABLE public.user_data TO manager;
          public          postgres    false    230            ?            1259    125694    user_data_user_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.user_data_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.user_data_user_id_seq;
       public          postgres    false    230                       0    0    user_data_user_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.user_data_user_id_seq OWNED BY public.user_data.user_id;
          public          postgres    false    229                       0    0    SEQUENCE user_data_user_id_seq    ACL     ?   GRANT USAGE ON SEQUENCE public.user_data_user_id_seq TO manager;
GRANT USAGE ON SEQUENCE public.user_data_user_id_seq TO admin;
          public          postgres    false    229            ?           2604    125643    business_center bc_id    DEFAULT     ~   ALTER TABLE ONLY public.business_center ALTER COLUMN bc_id SET DEFAULT nextval('public.business_center_bc_id_seq'::regclass);
 D   ALTER TABLE public.business_center ALTER COLUMN bc_id DROP DEFAULT;
       public          postgres    false    220    219    220            ?           2604    125612    client client_id    DEFAULT     t   ALTER TABLE ONLY public.client ALTER COLUMN client_id SET DEFAULT nextval('public.client_client_id_seq'::regclass);
 ?   ALTER TABLE public.client ALTER COLUMN client_id DROP DEFAULT;
       public          postgres    false    214    213    214            ?           2604    125619    client_type client_type_id    DEFAULT     ?   ALTER TABLE ONLY public.client_type ALTER COLUMN client_type_id SET DEFAULT nextval('public.client_type_client_type_id_seq'::regclass);
 I   ALTER TABLE public.client_type ALTER COLUMN client_type_id DROP DEFAULT;
       public          postgres    false    215    216    216            ?           2604    125708    company company_id    DEFAULT     x   ALTER TABLE ONLY public.company ALTER COLUMN company_id SET DEFAULT nextval('public.company_company_id_seq'::regclass);
 A   ALTER TABLE public.company ALTER COLUMN company_id DROP DEFAULT;
       public          postgres    false    231    232    232            ?           2604    125658     contact_person contact_person_id    DEFAULT     ?   ALTER TABLE ONLY public.contact_person ALTER COLUMN contact_person_id SET DEFAULT nextval('public.contact_person_contact_person_id_seq'::regclass);
 O   ALTER TABLE public.contact_person ALTER COLUMN contact_person_id DROP DEFAULT;
       public          postgres    false    221    222    222            ?           2604    125665    contract contract_id    DEFAULT     |   ALTER TABLE ONLY public.contract ALTER COLUMN contract_id SET DEFAULT nextval('public.contract_contract_id_seq'::regclass);
 C   ALTER TABLE public.contract ALTER COLUMN contract_id DROP DEFAULT;
       public          postgres    false    223    224    224            ?           2604    125674    document_delivery_sheet dds_id    DEFAULT     ?   ALTER TABLE ONLY public.document_delivery_sheet ALTER COLUMN dds_id SET DEFAULT nextval('public.document_delivery_sheet_dds_id_seq'::regclass);
 M   ALTER TABLE public.document_delivery_sheet ALTER COLUMN dds_id DROP DEFAULT;
       public          postgres    false    226    225    226            ?           2604    125683    individual_entrepreneur ie_id    DEFAULT     ?   ALTER TABLE ONLY public.individual_entrepreneur ALTER COLUMN ie_id SET DEFAULT nextval('public.individual_entrepreneur_ie_id_seq'::regclass);
 L   ALTER TABLE public.individual_entrepreneur ALTER COLUMN ie_id DROP DEFAULT;
       public          postgres    false    228    227    228            ?           2604    125628    metro_station metro_station_id    DEFAULT     ?   ALTER TABLE ONLY public.metro_station ALTER COLUMN metro_station_id SET DEFAULT nextval('public.metro_station_metro_station_id_seq'::regclass);
 M   ALTER TABLE public.metro_station ALTER COLUMN metro_station_id DROP DEFAULT;
       public          postgres    false    218    217    218            ?           2604    125603    role role_id    DEFAULT     l   ALTER TABLE ONLY public.role ALTER COLUMN role_id SET DEFAULT nextval('public.role_role_id_seq'::regclass);
 ;   ALTER TABLE public.role ALTER COLUMN role_id DROP DEFAULT;
       public          postgres    false    211    212    212            ?           2604    125593    service service_id    DEFAULT     x   ALTER TABLE ONLY public.service ALTER COLUMN service_id SET DEFAULT nextval('public.service_service_id_seq'::regclass);
 A   ALTER TABLE public.service ALTER COLUMN service_id DROP DEFAULT;
       public          postgres    false    210    209    210            ?           2604    125725    task task_id    DEFAULT     l   ALTER TABLE ONLY public.task ALTER COLUMN task_id SET DEFAULT nextval('public.task_task_id_seq'::regclass);
 ;   ALTER TABLE public.task ALTER COLUMN task_id DROP DEFAULT;
       public          postgres    false    234    233    234            ?           2604    125698    user_data user_id    DEFAULT     v   ALTER TABLE ONLY public.user_data ALTER COLUMN user_id SET DEFAULT nextval('public.user_data_user_id_seq'::regclass);
 @   ALTER TABLE public.user_data ALTER COLUMN user_id DROP DEFAULT;
       public          postgres    false    230    229    230            ?          0    125640    business_center 
   TABLE DATA           l   COPY public.business_center (bc_id, bc_name, bc_address, bc_passes, bc_clients_id, bc_metro_id) FROM stdin;
    public          postgres    false    220   `(      ?          0    125609    client 
   TABLE DATA           S   COPY public.client (client_id, client_type, client_name, client_bc_id) FROM stdin;
    public          postgres    false    214   D)      ?          0    125616    client_type 
   TABLE DATA           G   COPY public.client_type (client_type_id, client_type_name) FROM stdin;
    public          postgres    false    216   ?)      ?          0    125705    company 
   TABLE DATA           ?   COPY public.company (company_id, company_name, company_office_num, company_contacts_id, company_call_ahead, company_contract_id, company_contract_received, company_description, company_bc_id) FROM stdin;
    public          postgres    false    232   #*      ?          0    125655    contact_person 
   TABLE DATA           ?   COPY public.contact_person (contact_person_id, contact_person_firstname, contact_person_lastname, contact_person_phonenum, contact_person_company_id) FROM stdin;
    public          postgres    false    222   *+      ?          0    125662    contract 
   TABLE DATA           R   COPY public.contract (contract_id, contract_num, contract_service_id) FROM stdin;
    public          postgres    false    224   ?+      ?          0    125671    document_delivery_sheet 
   TABLE DATA           S   COPY public.document_delivery_sheet (dds_id, dds_dates, dds_client_id) FROM stdin;
    public          postgres    false    226   ],      ?          0    125680    individual_entrepreneur 
   TABLE DATA           ?   COPY public.individual_entrepreneur (ie_id, ie_firstname, ie_lastname, ie_phone, ie_contract_id, ie_office_num, ie_call_ahead, ie_contract_received, ie_description, ie_bc_id) FROM stdin;
    public          postgres    false    228   ?,      ?          0    125625    metro_station 
   TABLE DATA              COPY public.metro_station (metro_station_id, metro_station_name, metro_station_bc_id, metro_station_doc_condition) FROM stdin;
    public          postgres    false    218   ?-      ?          0    125600    role 
   TABLE DATA           2   COPY public.role (role_id, role_name) FROM stdin;
    public          postgres    false    212   B.      ?          0    125590    service 
   TABLE DATA           J   COPY public.service (service_id, service_name, service_price) FROM stdin;
    public          postgres    false    210   y.      ?          0    125722    task 
   TABLE DATA           ?   COPY public.task (task_id, task_condition, task_metro_id, task_start_date, task_close_date, task_execution_date, task_user_id) FROM stdin;
    public          postgres    false    234   */      ?          0    125695 	   user_data 
   TABLE DATA           C   COPY public.user_data (user_id, user_login, user_role) FROM stdin;
    public          postgres    false    230   ?/                 0    0    business_center_bc_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.business_center_bc_id_seq', 6, true);
          public          postgres    false    219                       0    0    client_client_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.client_client_id_seq', 12, true);
          public          postgres    false    213                       0    0    client_type_client_type_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.client_type_client_type_id_seq', 2, true);
          public          postgres    false    215                       0    0    company_company_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.company_company_id_seq', 6, true);
          public          postgres    false    231                       0    0 $   contact_person_contact_person_id_seq    SEQUENCE SET     R   SELECT pg_catalog.setval('public.contact_person_contact_person_id_seq', 7, true);
          public          postgres    false    221                       0    0    contract_contract_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.contract_contract_id_seq', 12, true);
          public          postgres    false    223                       0    0 "   document_delivery_sheet_dds_id_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('public.document_delivery_sheet_dds_id_seq', 12, true);
          public          postgres    false    225                       0    0 !   individual_entrepreneur_ie_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.individual_entrepreneur_ie_id_seq', 6, true);
          public          postgres    false    227                       0    0 "   metro_station_metro_station_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.metro_station_metro_station_id_seq', 7, true);
          public          postgres    false    217                       0    0    role_role_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.role_role_id_seq', 3, true);
          public          postgres    false    211                       0    0    service_service_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.service_service_id_seq', 8, true);
          public          postgres    false    209                       0    0    task_task_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.task_task_id_seq', 5, true);
          public          postgres    false    233                       0    0    user_data_user_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.user_data_user_id_seq', 5, true);
          public          postgres    false    229            ?           2606    125653 1   business_center business_center_bc_clients_id_key 
   CONSTRAINT     u   ALTER TABLE ONLY public.business_center
    ADD CONSTRAINT business_center_bc_clients_id_key UNIQUE (bc_clients_id);
 [   ALTER TABLE ONLY public.business_center DROP CONSTRAINT business_center_bc_clients_id_key;
       public            postgres    false    220            ?           2606    125651 +   business_center business_center_bc_name_key 
   CONSTRAINT     i   ALTER TABLE ONLY public.business_center
    ADD CONSTRAINT business_center_bc_name_key UNIQUE (bc_name);
 U   ALTER TABLE ONLY public.business_center DROP CONSTRAINT business_center_bc_name_key;
       public            postgres    false    220            ?           2606    125649 $   business_center business_center_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.business_center
    ADD CONSTRAINT business_center_pkey PRIMARY KEY (bc_id);
 N   ALTER TABLE ONLY public.business_center DROP CONSTRAINT business_center_pkey;
       public            postgres    false    220            ?           2606    125614    client client_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_pkey PRIMARY KEY (client_id);
 <   ALTER TABLE ONLY public.client DROP CONSTRAINT client_pkey;
       public            postgres    false    214            ?           2606    125623 ,   client_type client_type_client_type_name_key 
   CONSTRAINT     s   ALTER TABLE ONLY public.client_type
    ADD CONSTRAINT client_type_client_type_name_key UNIQUE (client_type_name);
 V   ALTER TABLE ONLY public.client_type DROP CONSTRAINT client_type_client_type_name_key;
       public            postgres    false    216            ?           2606    125621    client_type client_type_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.client_type
    ADD CONSTRAINT client_type_pkey PRIMARY KEY (client_type_id);
 F   ALTER TABLE ONLY public.client_type DROP CONSTRAINT client_type_pkey;
       public            postgres    false    216                       2606    125718 '   company company_company_contacts_id_key 
   CONSTRAINT     q   ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_company_contacts_id_key UNIQUE (company_contacts_id);
 Q   ALTER TABLE ONLY public.company DROP CONSTRAINT company_company_contacts_id_key;
       public            postgres    false    232                       2606    125720 '   company company_company_contract_id_key 
   CONSTRAINT     q   ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_company_contract_id_key UNIQUE (company_contract_id);
 Q   ALTER TABLE ONLY public.company DROP CONSTRAINT company_company_contract_id_key;
       public            postgres    false    232                       2606    125716    company company_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_pkey PRIMARY KEY (company_id);
 >   ALTER TABLE ONLY public.company DROP CONSTRAINT company_pkey;
       public            postgres    false    232            ?           2606    125660 "   contact_person contact_person_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.contact_person
    ADD CONSTRAINT contact_person_pkey PRIMARY KEY (contact_person_id);
 L   ALTER TABLE ONLY public.contact_person DROP CONSTRAINT contact_person_pkey;
       public            postgres    false    222            ?           2606    125669 "   contract contract_contract_num_key 
   CONSTRAINT     e   ALTER TABLE ONLY public.contract
    ADD CONSTRAINT contract_contract_num_key UNIQUE (contract_num);
 L   ALTER TABLE ONLY public.contract DROP CONSTRAINT contract_contract_num_key;
       public            postgres    false    224            ?           2606    125667    contract contract_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.contract
    ADD CONSTRAINT contract_pkey PRIMARY KEY (contract_id);
 @   ALTER TABLE ONLY public.contract DROP CONSTRAINT contract_pkey;
       public            postgres    false    224            ?           2606    125678 4   document_delivery_sheet document_delivery_sheet_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.document_delivery_sheet
    ADD CONSTRAINT document_delivery_sheet_pkey PRIMARY KEY (dds_id);
 ^   ALTER TABLE ONLY public.document_delivery_sheet DROP CONSTRAINT document_delivery_sheet_pkey;
       public            postgres    false    226            ?           2606    125693 B   individual_entrepreneur individual_entrepreneur_ie_contract_id_key 
   CONSTRAINT     ?   ALTER TABLE ONLY public.individual_entrepreneur
    ADD CONSTRAINT individual_entrepreneur_ie_contract_id_key UNIQUE (ie_contract_id);
 l   ALTER TABLE ONLY public.individual_entrepreneur DROP CONSTRAINT individual_entrepreneur_ie_contract_id_key;
       public            postgres    false    228            ?           2606    125691 <   individual_entrepreneur individual_entrepreneur_ie_phone_key 
   CONSTRAINT     {   ALTER TABLE ONLY public.individual_entrepreneur
    ADD CONSTRAINT individual_entrepreneur_ie_phone_key UNIQUE (ie_phone);
 f   ALTER TABLE ONLY public.individual_entrepreneur DROP CONSTRAINT individual_entrepreneur_ie_phone_key;
       public            postgres    false    228            ?           2606    125689 4   individual_entrepreneur individual_entrepreneur_pkey 
   CONSTRAINT     u   ALTER TABLE ONLY public.individual_entrepreneur
    ADD CONSTRAINT individual_entrepreneur_pkey PRIMARY KEY (ie_id);
 ^   ALTER TABLE ONLY public.individual_entrepreneur DROP CONSTRAINT individual_entrepreneur_pkey;
       public            postgres    false    228            ?           2606    125638 3   metro_station metro_station_metro_station_bc_id_key 
   CONSTRAINT     }   ALTER TABLE ONLY public.metro_station
    ADD CONSTRAINT metro_station_metro_station_bc_id_key UNIQUE (metro_station_bc_id);
 ]   ALTER TABLE ONLY public.metro_station DROP CONSTRAINT metro_station_metro_station_bc_id_key;
       public            postgres    false    218            ?           2606    125636 2   metro_station metro_station_metro_station_name_key 
   CONSTRAINT     {   ALTER TABLE ONLY public.metro_station
    ADD CONSTRAINT metro_station_metro_station_name_key UNIQUE (metro_station_name);
 \   ALTER TABLE ONLY public.metro_station DROP CONSTRAINT metro_station_metro_station_name_key;
       public            postgres    false    218            ?           2606    125634     metro_station metro_station_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.metro_station
    ADD CONSTRAINT metro_station_pkey PRIMARY KEY (metro_station_id);
 J   ALTER TABLE ONLY public.metro_station DROP CONSTRAINT metro_station_pkey;
       public            postgres    false    218            ?           2606    125605    role role_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.role
    ADD CONSTRAINT role_pkey PRIMARY KEY (role_id);
 8   ALTER TABLE ONLY public.role DROP CONSTRAINT role_pkey;
       public            postgres    false    212            ?           2606    125607    role role_role_name_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.role
    ADD CONSTRAINT role_role_name_key UNIQUE (role_name);
 A   ALTER TABLE ONLY public.role DROP CONSTRAINT role_role_name_key;
       public            postgres    false    212            ?           2606    125596    service service_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (service_id);
 >   ALTER TABLE ONLY public.service DROP CONSTRAINT service_pkey;
       public            postgres    false    210            ?           2606    125598     service service_service_name_key 
   CONSTRAINT     c   ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_service_name_key UNIQUE (service_name);
 J   ALTER TABLE ONLY public.service DROP CONSTRAINT service_service_name_key;
       public            postgres    false    210            
           2606    125732    task task_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.task
    ADD CONSTRAINT task_pkey PRIMARY KEY (task_id);
 8   ALTER TABLE ONLY public.task DROP CONSTRAINT task_pkey;
       public            postgres    false    234                       2606    125734    task task_task_metro_id_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.task
    ADD CONSTRAINT task_task_metro_id_key UNIQUE (task_metro_id);
 E   ALTER TABLE ONLY public.task DROP CONSTRAINT task_task_metro_id_key;
       public            postgres    false    234            ?           2606    125701    user_data user_data_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.user_data
    ADD CONSTRAINT user_data_pkey PRIMARY KEY (user_id);
 B   ALTER TABLE ONLY public.user_data DROP CONSTRAINT user_data_pkey;
       public            postgres    false    230                       2606    125703 "   user_data user_data_user_login_key 
   CONSTRAINT     c   ALTER TABLE ONLY public.user_data
    ADD CONSTRAINT user_data_user_login_key UNIQUE (user_login);
 L   ALTER TABLE ONLY public.user_data DROP CONSTRAINT user_data_user_login_key;
       public            postgres    false    230            ?           1259    125736    client_bc_id_idx    INDEX     K   CREATE INDEX client_bc_id_idx ON public.client USING btree (client_bc_id);
 $   DROP INDEX public.client_bc_id_idx;
       public            postgres    false    214            ?           1259    125737    client_name_idx    INDEX     I   CREATE INDEX client_name_idx ON public.client USING btree (client_name);
 #   DROP INDEX public.client_name_idx;
       public            postgres    false    214                       1259    125735    task_condition_idx    INDEX     M   CREATE INDEX task_condition_idx ON public.task USING btree (task_condition);
 &   DROP INDEX public.task_condition_idx;
       public            postgres    false    234                       2620    125811    business_center create_bc    TRIGGER     x   CREATE TRIGGER create_bc AFTER INSERT ON public.business_center FOR EACH ROW EXECUTE FUNCTION public.add_bc_to_metro();
 2   DROP TRIGGER create_bc ON public.business_center;
       public          postgres    false    220    257                       2620    125810    client create_client    TRIGGER     t   CREATE TRIGGER create_client AFTER INSERT ON public.client FOR EACH ROW EXECUTE FUNCTION public.add_client_to_bc();
 -   DROP TRIGGER create_client ON public.client;
       public          postgres    false    214    256                       2620    125808    company create_client_com    TRIGGER     ?   CREATE TRIGGER create_client_com AFTER UPDATE ON public.company FOR EACH ROW EXECUTE FUNCTION public.create_client_from_company();
 2   DROP TRIGGER create_client_com ON public.company;
       public          postgres    false    252    232                       2620    125807 (   individual_entrepreneur create_client_ie    TRIGGER     ?   CREATE TRIGGER create_client_ie AFTER INSERT ON public.individual_entrepreneur FOR EACH ROW EXECUTE FUNCTION public.create_client_from_ie();
 A   DROP TRIGGER create_client_ie ON public.individual_entrepreneur;
       public          postgres    false    228    249                       2620    125809    contact_person create_contacts    TRIGGER     ?   CREATE TRIGGER create_contacts AFTER INSERT ON public.contact_person FOR EACH ROW EXECUTE FUNCTION public.add_contacts_to_company();
 7   DROP TRIGGER create_contacts ON public.contact_person;
       public          postgres    false    222    251                       2620    125806    task update2_task    TRIGGER     ?   CREATE TRIGGER update2_task BEFORE UPDATE OF task_condition ON public.task FOR EACH ROW EXECUTE FUNCTION public.change_task_cour();
 *   DROP TRIGGER update2_task ON public.task;
       public          postgres    false    234    253    234                       2620    125805    task update_task    TRIGGER     ?   CREATE TRIGGER update_task BEFORE UPDATE OF task_close_date, task_user_id ON public.task FOR EACH ROW EXECUTE FUNCTION public.change_task_man();
 )   DROP TRIGGER update_task ON public.task;
       public          postgres    false    234    264    234    234                       2606    125738 (   business_center bc_metro_station_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.business_center
    ADD CONSTRAINT bc_metro_station_id_fkey FOREIGN KEY (bc_metro_id) REFERENCES public.metro_station(metro_station_id) ON DELETE RESTRICT;
 R   ALTER TABLE ONLY public.business_center DROP CONSTRAINT bc_metro_station_id_fkey;
       public          postgres    false    3305    218    220                       2606    125788    client client_type_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_type_id_fkey FOREIGN KEY (client_type) REFERENCES public.client_type(client_type_id) ON DELETE RESTRICT;
 D   ALTER TABLE ONLY public.client DROP CONSTRAINT client_type_id_fkey;
       public          postgres    false    216    3299    214                       2606    125748    company company_bc_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_bc_id_fkey FOREIGN KEY (company_bc_id) REFERENCES public.business_center(bc_id) ON DELETE RESTRICT;
 D   ALTER TABLE ONLY public.company DROP CONSTRAINT company_bc_id_fkey;
       public          postgres    false    220    232    3311                       2606    125743     company company_contract_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_contract_id_fkey FOREIGN KEY (company_contract_id) REFERENCES public.contract(contract_id) ON DELETE RESTRICT;
 J   ALTER TABLE ONLY public.company DROP CONSTRAINT company_contract_id_fkey;
       public          postgres    false    232    224    3317                       2606    125753 -   contact_person contact_person_company_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.contact_person
    ADD CONSTRAINT contact_person_company_id_fkey FOREIGN KEY (contact_person_company_id) REFERENCES public.company(company_id) ON DELETE RESTRICT;
 W   ALTER TABLE ONLY public.contact_person DROP CONSTRAINT contact_person_company_id_fkey;
       public          postgres    false    222    3335    232                       2606    125758 !   contract contract_service_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.contract
    ADD CONSTRAINT contract_service_id_fkey FOREIGN KEY (contract_service_id) REFERENCES public.service(service_id) ON DELETE RESTRICT;
 K   ALTER TABLE ONLY public.contract DROP CONSTRAINT contract_service_id_fkey;
       public          postgres    false    3285    224    210                       2606    125763 *   document_delivery_sheet dds_client_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.document_delivery_sheet
    ADD CONSTRAINT dds_client_id_fkey FOREIGN KEY (dds_client_id) REFERENCES public.client(client_id) ON DELETE RESTRICT;
 T   ALTER TABLE ONLY public.document_delivery_sheet DROP CONSTRAINT dds_client_id_fkey;
       public          postgres    false    214    3295    226                       2606    125773 %   individual_entrepreneur ie_bc_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.individual_entrepreneur
    ADD CONSTRAINT ie_bc_id_fkey FOREIGN KEY (ie_bc_id) REFERENCES public.business_center(bc_id) ON DELETE RESTRICT;
 O   ALTER TABLE ONLY public.individual_entrepreneur DROP CONSTRAINT ie_bc_id_fkey;
       public          postgres    false    228    3311    220                       2606    125768 +   individual_entrepreneur ie_contract_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.individual_entrepreneur
    ADD CONSTRAINT ie_contract_id_fkey FOREIGN KEY (ie_contract_id) REFERENCES public.contract(contract_id) ON DELETE RESTRICT;
 U   ALTER TABLE ONLY public.individual_entrepreneur DROP CONSTRAINT ie_contract_id_fkey;
       public          postgres    false    224    3317    228                       2606    125783    task tusk_user_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.task
    ADD CONSTRAINT tusk_user_id_fkey FOREIGN KEY (task_user_id) REFERENCES public.user_data(user_id) ON DELETE RESTRICT;
 @   ALTER TABLE ONLY public.task DROP CONSTRAINT tusk_user_id_fkey;
       public          postgres    false    234    3327    230                       2606    125778    user_data user_role_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.user_data
    ADD CONSTRAINT user_role_fkey FOREIGN KEY (user_role) REFERENCES public.role(role_id) ON DELETE RESTRICT;
 B   ALTER TABLE ONLY public.user_data DROP CONSTRAINT user_role_fkey;
       public          postgres    false    230    3289    212            ?           3256    125801    task check_tasks    POLICY     J  CREATE POLICY check_tasks ON public.task FOR SELECT TO manager, courier USING ((((( SELECT user_data.user_login
   FROM public.user_data
  WHERE (user_data.user_id = task.task_user_id)))::text = CURRENT_USER) OR (( SELECT user_data.user_role
   FROM public.user_data
  WHERE ((user_data.user_login)::text = CURRENT_USER)) = 2)));
 (   DROP POLICY check_tasks ON public.task;
       public          postgres    false    234    230    230    230    234            ?           3256    125800    user_data check_user_data    POLICY     ~   CREATE POLICY check_user_data ON public.user_data FOR SELECT TO manager, courier USING (((user_login)::text = CURRENT_USER));
 1   DROP POLICY check_user_data ON public.user_data;
       public          postgres    false    230    230            ?           3256    125804    task ins_tasks    POLICY     P   CREATE POLICY ins_tasks ON public.task FOR INSERT TO manager WITH CHECK (true);
 &   DROP POLICY ins_tasks ON public.task;
       public          postgres    false    234            ?           0    125722    task    ROW SECURITY     2   ALTER TABLE public.task ENABLE ROW LEVEL SECURITY;          public          postgres    false    234            ?           3256    125802    task up_tasks    POLICY     ?   CREATE POLICY up_tasks ON public.task TO courier USING (((( SELECT user_data.user_login
   FROM public.user_data
  WHERE (user_data.user_id = task.task_user_id)))::text = CURRENT_USER));
 %   DROP POLICY up_tasks ON public.task;
       public          postgres    false    230    230    234    234            ?           3256    125803    task upd_tasks    POLICY     ]   CREATE POLICY upd_tasks ON public.task FOR UPDATE TO manager USING (true) WITH CHECK (true);
 &   DROP POLICY upd_tasks ON public.task;
       public          postgres    false    234            ?           0    125695 	   user_data    ROW SECURITY     7   ALTER TABLE public.user_data ENABLE ROW LEVEL SECURITY;          public          postgres    false    230            ?   ?   x?]??J?@??s?"?c?N???????6.?tˀ?V

ڊ?/?,.,?g8?F?q??4??.??؟4-??!M???߱K??V?Ĵp??b??M??????8?G??;~s??Bv?1Z???֔V
?H?j?~Mj+??PH?rř?~q?o~?y8\s?'|??r?㐉?:<?[X?G}p??^%5??-??
??9?UT?Z?RNR??m~?      ?   ?   x?3?4??0?¾??x?!?H`????.???1Hh)???b???v\?{aP?	D?V????&Nc.S?? w???{/?q?p?qA??}?h?9?????i?ed??Y?@VDIQbf?C /8??h??!ȼy??B\h?eh2py1z\\\ ?+R?      ?      x?3??t?2?t??-H̫?????? 1$?      ?   ?   x?-??JQ??s?b{5?ݿ??D-l,?XX??]?,?Rl?7XVC?l^??ef#??s?9??W??9B2?	?Z|g)S?ܲfqǖ??f+s?*?e.?HG-w?ý????V?%r?bp7B{??bO???*d??n???8A?&8?|??Z?,36U??le?J??8??k?.????Xm!7????????(uc?_u?:?g}?"???΃??5?2\bq@L\~?A?e?n?WQ?????s{???      ?   ?   x?=?A?@???F?L????a?K6?[????????j??{??"Vq???u??tR?e?7?X1j;<h??=.???W6????*Ƹ6?u??s??r?	?4mθ?
U?j???L?`?;?Np??`n?[??????x?*U6??t??w?-??ߑk??m<?Zc$??@U?Z{z?      ?   Y   x?E???0??0U???t?9?F??w??F?y??? ????Bg 
???3??ɁQ8x/?l7?[?㹫?????I'wʎ?oN??? )      ?   @   x??9 1????Z?$???pi??DR?a?f?t?L3Yf??昃j?+R?P^)?? 	??      ?   ?   x?U?AN1??? P??fן?r?'AA??ȑp??J
?6|??G?I6?Ʋ,?T???5{?+??V?і?1+)%?!O?-?U?,Dp??????/?M?O??)?6?QC??q`????/5??pAFCBgW#1W?}??ե??5i????gQ
?|?R?p???'? ??1^#??bS??7?Fiw?}?mɝYJ0??????a~B?9??      ?   ?   x?E?=
?@???S؋B6????m??d	DZ? ^a?Bb?oo?,d???{?Z?/?Clг?gkY?T?DO~0U?)??]l?a?-?'xq?:????@?C??n0?ǋ?\??x??@u?I-KS??	????Bc??J+՞s?6?|ֹf)      ?   '   x?3?L?/-?L-?2??M?KL??9Sr3??b???? ?	U      ?   ?   x???1?0E??:???8[/҆1?s?@?*Z??}#R?Fj?f??|??[?0p͎??*4
-zvxs??W???0??????We>x?e?-E?7D?I???)B?	Y$H.?f?ܥX.?vf???"b? ?O?=??C???I?(p?h?{?·?9}?r)?5|V?      ?   U   x?}??	?0D???V$???UXA:	?]W%???r????&?E??v?z??%?_I?DD??I??=?+??k?l??Ԝm%y ߶"C      ?   F   x??9?@ ?c?a?_l ? ?????????]o?p댇?A???k0ʊ?~ ?B???+熈??q?     