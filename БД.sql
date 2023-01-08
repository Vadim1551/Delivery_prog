SET SESSION AUTHORIZATION postgres;

DROP TABLE IF EXISTS public.Role CASCADE;
DROP TABLE IF EXISTS public.Service CASCADE;
DROP TABLE IF EXISTS public.Metro_station CASCADE;
DROP TABLE IF EXISTS public.Business_center CASCADE;
DROP TABLE IF EXISTS public.Client CASCADE;
DROP TABLE IF EXISTS public.Client_type CASCADE;
DROP TABLE IF EXISTS public.Company CASCADE;
DROP TABLE IF EXISTS public.Individual_entrepreneur CASCADE;
DROP TABLE IF EXISTS public.User_data CASCADE;
DROP TABLE IF EXISTS public.Contact_person CASCADE;
DROP TABLE IF EXISTS public.Contract CASCADE;
DROP TABLE IF EXISTS public.Task CASCADE;
DROP TABLE IF EXISTS public.Document_delivery_sheet CASCADE;


CREATE TABLE public.Service
(
    service_id serial PRIMARY KEY,
    service_name character varying(50) UNIQUE NOT NULL,
    service_price money NOT NULL,
    CHECK (service_price > 0::money)
) WITHOUT OIDS;

CREATE TABLE IF NOT EXISTS public.Role
(
    role_id serial PRIMARY KEY,
    role_name character varying(7) UNIQUE NOT NULL
) WITHOUT OIDS;

CREATE TABLE IF NOT EXISTS public.Client
(
    client_id serial PRIMARY KEY,
    client_type smallint NOT NULL,
    client_name character varying(50) NOT NULL,
    client_BC_id integer NOT NULL
) WITHOUT OIDS;

CREATE TABLE IF NOT EXISTS public.Client_type
(
    client_type_id serial PRIMARY KEY,
    client_type_name character varying(8) UNIQUE
) WITHOUT OIDS;

CREATE TABLE IF NOT EXISTS public.Metro_station
(
    metro_station_id serial PRIMARY KEY,
    metro_station_name character varying(30) NOT NULL UNIQUE ,
    metro_station_BC_id integer[] UNIQUE,
    metro_station_doc_condition "char" NOT NULL DEFAULT '-'::"char"
    CHECK (metro_station_doc_condition = '-' OR metro_station_doc_condition = '+')
) WITHOUT OIDS;

CREATE TABLE IF NOT EXISTS public.Business_center
(
    BC_id serial PRIMARY KEY,
    BC_name character varying(30) NOT NULL UNIQUE ,
    BC_address character varying(50) NOT NULL,
    BC_passes "char" NOT NULL DEFAULT '-'::"char",
    BC_clients_id integer[] UNIQUE,
    BC_metro_id integer NOT NULL
    CHECK (BC_passes = '-' OR BC_passes = '+')
) WITHOUT OIDS;

CREATE TABLE IF NOT EXISTS public.Contact_person
(
    contact_person_id serial PRIMARY KEY,
    contact_person_firstName character varying(30) NOT NULL,
    contact_person_lastName character varying(30) NOT NULL,
    contact_person_phoneNum numeric(11,0) NOT NULL,
    contact_person_company_id integer NOT NULL
) WITHOUT OIDS;

CREATE TABLE IF NOT EXISTS public.Contract
(
    contract_id serial PRIMARY KEY,
    contract_num numeric(10, 0) NOT NULL UNIQUE,
    contract_service_id smallint
) WITHOUT OIDS;

CREATE TABLE IF NOT EXISTS public.Document_delivery_sheet
(
    DDS_id serial PRIMARY KEY,
    DDS_dates date[],
    DDS_client_id integer NOT NULL
) WITHOUT OIDS;

CREATE TABLE IF NOT EXISTS public.Individual_entrepreneur
(
    IE_id serial PRIMARY KEY,
    IE_firstName character varying(30) NOT NULL,
    IE_lastName character varying(30) NOT NULL,
    IE_phone numeric(11,0) NOT NULL UNIQUE,
    IE_contract_id integer NOT NULL UNIQUE,
    IE_office_num character varying(10),
    IE_call_ahead "char" DEFAULT '-'::"char",
    IE_contract_received "char" DEFAULT '-'::"char",
    IE_description character varying(100),
    IE_BC_id integer NOT NULL
    CHECK (IE_call_ahead = '-' OR IE_call_ahead = '+')
    CHECK (IE_contract_received = '-' OR IE_contract_received = '+')
) WITHOUT OIDS;

CREATE TABLE IF NOT EXISTS public.User_data
(
    user_id serial PRIMARY KEY,
    user_login character varying(20) UNIQUE,
    user_role smallint NOT NULL
    CHECK (user_login <> 'postgres')
) WITHOUT OIDS;

CREATE TABLE IF NOT EXISTS public.Company
(
    company_id serial PRIMARY KEY,
    company_name character varying(30) NOT NULL,
    company_office_num character varying(10) NOT NULL,
    company_contacts_id integer[] UNIQUE,
    company_call_ahead "char" NOT NULL DEFAULT '-'::"char",
    company_contract_id integer NOT NULL UNIQUE ,
    company_contract_received "char" NOT NULL DEFAULT '-'::"char",
    company_description character varying(100),
    company_BC_id integer NOT NULL
    CHECK (company_call_ahead = '-' OR company_call_ahead = '+')
    CHECK (company_contract_received = '-' OR company_contract_received = '+')
) WITHOUT OIDS;

CREATE TABLE IF NOT EXISTS public.Task
(
    task_id serial PRIMARY KEY,
    task_condition "char" NOT NULL DEFAULT '-'::"char",
    task_metro_id integer[] NOT NULL UNIQUE,
    task_start_date date NOT NULL DEFAULT now(),
    task_close_date date NOT NULL,
    task_execution_date date,
    task_user_id integer NOT NULL
    CHECK (task_condition = '-' OR task_condition = '+')
) WITHOUT OIDS;

--ИНДЕКСАЦИЯ ЧАСТОИСПОЛЬЗУЕМЫХ ПОЛЕЙ
CREATE INDEX task_condition_idx ON Task (task_condition);
CREATE INDEX client_Bc_id_idx ON Client (client_BC_id);
CREATE INDEX client_name_idx ON Client (client_name);

ALTER TABLE public.Business_center
    ADD CONSTRAINT BC_metro_station_id_fkey FOREIGN KEY (BC_metro_id)
        REFERENCES public.Metro_station (metro_station_id)
        ON UPDATE NO ACTION
        ON DELETE RESTRICT;

ALTER TABLE public.Company
    ADD CONSTRAINT Company_contract_id_fkey FOREIGN KEY (company_contract_id)
        REFERENCES public.Contract (contract_id)
        ON UPDATE NO ACTION
        ON DELETE RESTRICT,

    ADD CONSTRAINT Company_BC_id_fkey FOREIGN KEY (company_BC_id)
        REFERENCES public.Business_center (bc_id)
        ON UPDATE NO ACTION
        ON DELETE RESTRICT;

ALTER TABLE public.Contact_person
    ADD CONSTRAINT Contact_person_company_id_fkey FOREIGN KEY (contact_person_company_id)
        REFERENCES public.Company (company_id)
        ON UPDATE NO ACTION
        ON DELETE RESTRICT;

ALTER TABLE public.Contract
    ADD CONSTRAINT Contract_service_id_fkey FOREIGN KEY (contract_service_id)
        REFERENCES public.Service (service_id)
        ON UPDATE NO ACTION
        ON DELETE RESTRICT;

ALTER TABLE public.Document_delivery_sheet
    ADD CONSTRAINT DDS_client_id_fkey FOREIGN KEY (DDS_client_id)
        REFERENCES public.Client (client_id)
        ON UPDATE NO ACTION
        ON DELETE RESTRICT;

ALTER TABLE public.Individual_entrepreneur
    ADD CONSTRAINT IE_contract_id_fkey FOREIGN KEY (IE_contract_id)
        REFERENCES public.Contract (contract_id)
        ON UPDATE NO ACTION
        ON DELETE RESTRICT,

    ADD CONSTRAINT IE_BC_id_fkey FOREIGN KEY (IE_BC_id)
        REFERENCES public.Business_center (bc_id)
        ON UPDATE NO ACTION
        ON DELETE RESTRICT;

ALTER TABLE public.User_data
    ADD CONSTRAINT User_role_fkey FOREIGN KEY (user_role)
        REFERENCES public.Role (role_id)
        ON UPDATE NO ACTION
        ON DELETE RESTRICT;

ALTER TABLE public.Task
    ADD  CONSTRAINT tusk_user_id_fkey FOREIGN KEY (task_user_id)
        REFERENCES public.User_data (user_id)
        ON UPDATE NO ACTION
        ON DELETE RESTRICT;

ALTER TABLE public.Client
    ADD  CONSTRAINT Client_type_id_fkey FOREIGN KEY (client_type)
        REFERENCES public.Client_type (client_type_id)
        ON UPDATE NO ACTION
        ON DELETE RESTRICT;

INSERT INTO public.Service (service_name, service_price)
VALUES
	('Доступ в интернет со скоростью 5 мбит/c',    1000.00),
	('Доступ в интернет со скоростью 10 мбит/c',   1200.00),
	('Доступ в интернет со скоростью 50 мбит/c',   2000.00),
	('Доступ в интернет со скоростью 100 мбит/c',  5000.00),
	('Доступ в интернет со скоростью 300 мбит/c',  12000.00),
	('Доступ в интернет со скоростью 500 мбит/c',  15000.00),
	('Доступ в интернет со скоростью 1000 мбит/c', 25000.00);

INSERT INTO public.Contract (contract_num, contract_service_id)
VALUES
	(1234567890, 1),
	(2234567890,2),
	(3234567890,3),
	(4234567890,4),
	(5234567890,5),
	(6234567890,6),
	(7234567890,7),
	(5234227890,2),
	(6234566789,1),
	(7234647890,1),
	(1114566789,3),
	(6234566666,4);

INSERT INTO public.Role (role_name)
VALUES
	('courier'),
	('manager'),
	('admin');

INSERT INTO public.Metro_station (metro_station_name)
VALUES
	('Новокосино'),
	('Новогиреево'),
	('Перово'),
	('Площадь Ильича'),
	('Авиамоторная');

INSERT INTO public.Client_type ( client_type_name)
VALUES
    ('IE'),
	('Company');


INSERT INTO public.User_data (user_login, user_role)
VALUES
    ('misterkolbaskin142', 3),
	('bosov123'          , 2),
	('boba1459'          , 1),
	('slavik14'          , 1);



DROP OWNED BY admin;
DROP ROLE IF EXISTS admin;
CREATE ROLE admin SUPERUSER CREATEROLE;

DROP OWNED BY manager;
DROP ROLE IF EXISTS manager;
CREATE ROLE manager;


DROP OWNED BY courier;
DROP ROLE IF EXISTS courier;
CREATE ROLE courier;


DROP USER IF EXISTS misterkolbaskin142;
CREATE USER misterkolbaskin142 IN ROLE admin ENCRYPTED PASSWORD '110adbfafja';
ALTER USER misterkolbaskin142 SUPERUSER;


DROP USER IF EXISTS bosov123;
CREATE USER bosov123 IN ROLE manager ENCRYPTED PASSWORD 'giveOneChance22';

DROP USER IF EXISTS boba1459;
CREATE USER boba1459 IN ROLE courier ENCRYPTED PASSWORD 'qwerty12';

DROP USER IF EXISTS slavik14;
CREATE USER slavik14 IN ROLE courier ENCRYPTED PASSWORD 'posi1134';


GRANT ALL ON ALL TABLES IN SCHEMA public TO admin;

GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO manager, admin;

GRANT UPDATE ON TABLE business_center, individual_entrepreneur, contact_person, company, client, metro_station TO manager;
GRANT INSERT ON TABLE business_center, individual_entrepreneur, contract, contact_person, company,
    client, metro_station, service, document_delivery_sheet TO manager;

GRANT UPDATE (task_metro_id, task_close_date, task_user_id) ON TABLE task TO manager;
GRANT INSERT (task_metro_id, task_close_date, task_user_id) ON TABLE task TO manager;
GRANT DELETE ON TABLE task TO manager;

GRANT SELECT ON TABLE business_center, task, individual_entrepreneur, contract, contact_person, company, client,
                        client_type, document_delivery_sheet, metro_station, service, user_data TO courier, manager;

GRANT UPDATE (task_condition) ON task TO courier;

GRANT UPDATE (dds_dates) ON document_delivery_sheet TO courier;


ALTER TABLE Task ENABLE ROW LEVEL SECURITY;
ALTER TABLE User_data ENABLE ROW LEVEL SECURITY;

--Пользователь видит только свои данные в таблице User_data
CREATE POLICY check_user_data ON User_data
    FOR SELECT TO courier, manager
    USING(
         user_login = current_user
    );

CREATE POLICY check_tasks ON Task
    FOR SELECT TO courier, manager
    USING(
        --Исполнитель задания может его просматривать
         (SELECT user_login
         FROM User_data
         WHERE (user_id = Task.task_user_id)) = current_user
             OR
         --Менеджеры видят все задания
         (SELECT user_role FROM User_data WHERE (user_login = current_user)) = 2
    );

CREATE POLICY UP_tasks ON Task TO courier
    USING (
         (SELECT user_login
         FROM User_data
         WHERE (user_id = Task.task_user_id)) = current_user
        );

CREATE POLICY upd_tasks ON Task
    FOR UPDATE TO manager
    USING (true)
    WITH CHECK (TRUE);

CREATE POLICY ins_tasks ON Task
    FOR INSERT TO manager
    WITH CHECK (TRUE);

-- Триггерная функция не дающая измеенить выполненное задание менеджеру.
CREATE OR REPLACE FUNCTION change_task_man()
    RETURNS TRIGGER AS
    $$
    BEGIN
        --ТОЛЬКО АДМИН МОЖЕТ МЕНЯТЬ ВЫПОЛНЕННОЕ ЗАДАНИЕ
        IF (OLD.task_condition = '+' AND (SELECT user_role FROM user_data WHERE user_login = current_user) <> 3) THEN
            RAISE EXCEPTION 'Выполненное задание нельзя изменить!';
        ELSE RETURN NEW;
        END IF;
    END
    $$
    LANGUAGE plpgsql;

-- Триггерная функция не дающая измеенить выполненное или чужое задание курьеру, а так же автоматически ставящая дату завершения задания.
CREATE OR REPLACE FUNCTION change_task_cour()
    RETURNS TRIGGER AS
    $$
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
    $$
    LANGUAGE plpgsql;

--ТРИГГЕР СРАБАТЫВАЮЩИЙ ПЕРЕД ОБНОВЛЕНИЕМ task_close_date, task_user_id ТАБЛИЦЫ Task
CREATE OR REPLACE TRIGGER update_task
    BEFORE UPDATE OF task_close_date, task_user_id ON Task
    FOR EACH ROW
    EXECUTE FUNCTION change_task_man();

--ТРИГГЕР СРАБАТЫВАЮЩИЙ ПЕРЕД ОБНОВЛЕНИЕМ task_condition ТАБЛИЦЫ Task
CREATE OR REPLACE TRIGGER update2_task
    BEFORE UPDATE OF task_condition ON Task
    FOR EACH ROW
    EXECUTE FUNCTION change_task_cour();

--ПРОЦЕДУРА УДАЛЕНИЯ ЗАДАНИЙ ВЫПОЛНЕННЫХ БОЛЛЕ 6 МЕСЯЦОВ НАЗАД
CREATE OR REPLACE PROCEDURE clear_tasks()
    AS
    $$
    BEGIN
        DELETE FROM Task WHERE(now() - task_execution_date >= INTERVAL '6 MONTH');
    END;
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE clear_tasks() TO manager;

--(ТРАНЗАКЦИЯ) ПРОЦЕДУРА для удаления юзера
CREATE OR REPLACE PROCEDURE delete_user(login varchar(20))
    AS
    $$
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
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE delete_user(login varchar(20)) TO admin;

--ТРИГГЕРНАЯ ФУНКЦИЯ СОЗДАЕТ КЛИЕНТА ПОСЛЕ СОЗДАНИЯ IE
CREATE OR REPLACE FUNCTION create_client_from_ie()
    RETURNS TRIGGER AS
    $$
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
    $$
    LANGUAGE plpgsql;

--ТРИГГЕР СРАБАТЫВАЮЩИЙ ПРИ ДОБАВЛЕНИИ ДАННЫХ В ТАБЛИЦУ Individual_entrepreneur
CREATE OR REPLACE TRIGGER create_client_IE
    AFTER INSERT ON Individual_entrepreneur
    FOR EACH ROW
    EXECUTE FUNCTION create_client_from_ie();

--ТРИГГЕРНАЯ ФУНКЦИЯ СОЗДАЕТ КЛИЕНТА ПОСЛЕ ДОБАВЛЕНИЯ В КОМПАНИЮ КОНТАКТНЫХ ЛИЦ.
CREATE OR REPLACE FUNCTION create_client_from_company()
    RETURNS TRIGGER AS
    $$
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
    $$
    LANGUAGE plpgsql;

--ТРИГГЕР СРАБАТЫВАЮЩИЙ ПРИ ОБНОВЛЕНИИ ДАННЫХ В ТАБЛИЦЕ Company
CREATE OR REPLACE TRIGGER create_client_Com
    AFTER UPDATE ON Company
    FOR EACH ROW
    EXECUTE FUNCTION create_client_from_company();

--ТРИГГЕРНАЯ ФУНКЦИЯ ДОБАВЛЕНИЯ КОНТАКТНЫХ ЛИЦ В КОМПАНИЮ, ПРИ СОЗДАНИИ КОНТАКТНЫХ ЛИЦ(КОНТАКТЫ СОЗДАЮТСЯ ПОСЛЕ СОЗДАНИЯ КОМПАНИИ)
CREATE OR REPLACE FUNCTION add_contacts_to_company()
    RETURNS TRIGGER AS
    $$
    DECLARE
        contact_id INTEGER;
        com_id INTEGER;
    BEGIN
        contact_id := NEW.contact_person_id;
        com_id := NEW.contact_person_company_id;
        EXECUTE format('UPDATE public.Company SET company_contacts_id = company_contacts_id || %s WHERE company_id = %s;', contact_id, com_id);
        RETURN NEW;
    END;
    $$
    LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER create_Contacts
    AFTER INSERT ON public.Contact_person
    FOR EACH ROW
    EXECUTE FUNCTION add_contacts_to_company();

--(ТРАНЗАКЦИЯ)ПРОЦЕДУРА ДЛЯ СОЗДАНИЯ ПОЗЛОВАТЕЛЯ
CREATE OR REPLACE PROCEDURE create_user(login varchar(20), id_role INT, pass varchar(20))
    AS
    $$
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
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE create_user(login varchar(20), role INT, pass varchar(20)) TO admin;


--ТРИГГЕРНАЯ ФУНКЦИЯ АВТОМАТИЧЕСКОГО ДОБАВЛЕНИЯ КЛИЕНТА В БЦ
CREATE OR REPLACE FUNCTION add_client_to_bc()
    RETURNS TRIGGER
    AS
    $$
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
    $$
    LANGUAGE plpgsql;


--ТРИГГЕР СРАБАТЫВАЮЩИЙ ПОСЛЕ ДОБАВЛЕНИЯ ЗАПИСИ В ТАБЛИЦУ Client
CREATE OR REPLACE TRIGGER create_Client
    AFTER INSERT ON public.Client
    FOR EACH ROW
    EXECUTE FUNCTION add_client_to_bc();

--ТРИГГЕРНАЯ ФУНКЦИЯ АВТОМАТИЧЕСКОГО ДОБАВЛЕНИЯ БЦ К МЕТРО
CREATE OR REPLACE FUNCTION add_bc_to_metro()
    RETURNS TRIGGER
    AS
    $$
    DECLARE
        bc_id INT;
        bc_metro_id INT;
    BEGIN
        bc_id := NEW.bc_id;
        bc_metro_id := NEW.bc_metro_id;
        EXECUTE format('UPDATE public.Metro_station SET metro_station_bc_id = metro_station_bc_id || %s WHERE metro_station_id = %s;', bc_id, bc_metro_id);
        RETURN NEW;
    END;
    $$
    LANGUAGE plpgsql;

--ТРИГГЕР СРАБАТЫВАЮЩИЙ ПОСЛЕ ДОБАВЛЕНИЯ ЗАПИСИ В ТАБЛИЦУ Business_center
CREATE OR REPLACE TRIGGER create_BC
    AFTER INSERT ON public.Business_center
    FOR EACH ROW
    EXECUTE FUNCTION add_bc_to_metro();

GRANT EXECUTE ON PROCEDURE clear_tasks() TO manager;


--ФУНКЦИЯ КОТОРАЯ ДОБАВЛЯЕТ ЗАПИСЬ В ТАБЛИЦУ DDS
CREATE OR REPLACE FUNCTION add_date_to_DDS(client_id INT)
    RETURNS VOID
    AS
    $$
    DECLARE
        date DATE;
        mas DATE[];
    BEGIN
        date := now();
        mas := (SELECT dds_dates FROM Document_delivery_sheet WHERE DDS_client_id = client_id);
        mas := mas || date;
        EXECUTE format('UPDATE public.Document_delivery_sheet SET dds_dates = %L WHERE dds_client_id = %s;', mas, client_id);
    END;
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON FUNCTION add_date_to_DDS(client_id INT) TO courier;


--ПРОЦЕДУРА СОЗДАНИЯ МЕТРО
CREATE OR REPLACE PROCEDURE create_metro(station_name varchar(30))
    AS
    $$
    BEGIN
        EXECUTE format('INSERT INTO public.Metro_station (metro_station_name) VALUES (%L);', station_name);
    END;
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE create_metro(station_name varchar(30)) TO manager;


--ПРОЦЕДУРА СОЗДАНИЯ БЦ
CREATE OR REPLACE PROCEDURE create_bc(bc_name varchar(30), bc_address varchar(50), passes CHAR, metro_id INT)
    AS
    $$
    BEGIN
        EXECUTE format('INSERT INTO public.Business_center (BC_name, BC_address,BC_passes, BC_metro_id) VALUES (%L, %L, %L, %L);', bc_name, bc_address, passes, metro_id);
    END;
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE create_bc(bc_name varchar(30), bc_address varchar(50), passes CHAR, metro_id INT) TO manager;


--ПРОЦЕДУРА СОЗДАНИЯ КОНТРАКТА
CREATE OR REPLACE PROCEDURE create_contract(num NUMERIC(10,0), service_id INT)
    AS
    $$
    BEGIN
        EXECUTE format('INSERT INTO public.Contract (contract_num, contract_service_id) VALUES (%L, %L);',num, service_id);
    END;
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE create_contract(num NUMERIC(10,0), service_id INT) TO manager;



--ПРОЦЕДУРА СОЗДАНИЯ И.П.
CREATE OR REPLACE PROCEDURE create_ie(fname varchar(30), lname varchar(30), phone NUMERIC(11,0), contract_id INT,
                    office_num VARCHAR(10), call_ahead CHAR, contract_received CHAR, description varchar(100), bc_id INT)
    AS
    $$
    BEGIN
        EXECUTE format('INSERT INTO public.Individual_entrepreneur ' ||
                       '(ie_firstname, ie_lastname, ie_phone, ie_contract_id, ' ||
                       'ie_office_num, ie_description, ie_call_ahead, ie_contract_received, IE_BC_id) ' ||
                       'VALUES (%L, %L, %L, %L, %L, %L, %L, %L, %L);',
            fname, lname, phone, contract_id,office_num, description, call_ahead, contract_received, bc_id);
    END;
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE create_ie(fname varchar(30), lname varchar(30), phone NUMERIC(11,0), contract_id INT,
                    office_num VARCHAR(10), call_ahead CHAR, contract_received CHAR, description varchar(100), bc_id INT)
    TO manager;


--ПРОЦЕДУРА СОЗДАНИЯ КОМПАНИИ
CREATE OR REPLACE PROCEDURE create_company(name varchar(30),  office_num VARCHAR(10), call_ahead CHAR, contract_id INT,
                    contract_received CHAR, description varchar(100), bc_id INT)
    AS
    $$
    BEGIN
        EXECUTE format('INSERT INTO public.Company ' ||
                       '(company_name, company_office_num, company_call_ahead, company_contract_id, ' ||
                       'company_contract_received, company_description, company_bc_id) ' ||
                       'VALUES (%L, %L, %L, %L, %L, %L, %L);',
            name, office_num, call_ahead, contract_id,contract_received, description, bc_id);
    END;
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE create_company(name varchar(30),  office_num VARCHAR(10), call_ahead CHAR, contract_id INT,
                    contract_received CHAR, description varchar(100), bc_id INT) TO manager;


--ПРОЦЕДУРА СОЗДАНИЯ КОНАКТНОГО ЛИЦА
CREATE OR REPLACE PROCEDURE create_contact_person(fname varchar(30), lname varchar(30), phone NUMERIC(11,0), company_id INT)
    AS
    $$
    BEGIN
        EXECUTE format('INSERT INTO public.Contact_person ' ||
                       '(contact_person_firstname, contact_person_lastname, ' ||
                       'contact_person_phonenum, contact_person_company_id) ' ||
                       'VALUES (%L, %L, %L, %L);',
            fname, lname, phone, company_id);
    END;
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE create_contact_person(fname varchar(30), lname varchar(30), phone NUMERIC(11,0), company_id INT) TO manager;

--ПРОЦЕДУРА СОЗДАНИЯ ЗАДАНИЯ
CREATE OR REPLACE PROCEDURE create_task(metro_id INTEGER[], close_date DATE, user_id INTEGER)
    AS
    $$
    BEGIN
        EXECUTE format('INSERT INTO public.Task ' ||
                       '(task_metro_id, task_close_date, ' ||
                       'task_user_id) ' ||
                       'VALUES (%L, %L, %L);',
            metro_id, close_date,user_id);
    END;
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE create_task(metro_id INTEGER[], close_date DATE, user_id INTEGER) TO manager;

--ПРОЦЕДУРА СОЗДАНИЯ УСЛУГИ
CREATE OR REPLACE PROCEDURE create_service(name varchar(50), price INT)
    AS
    $$
    BEGIN
        EXECUTE format('INSERT INTO public.Service ' ||
                       '(service_name, service_price) ' ||
                       'VALUES (%L, %L);',
            name, price::money);
    END;
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE create_service(name varchar(50), price Money) TO manager;


--ПРОЦЕДУРА ИЗМЕНЕНИЯ СОСТОЯНИЯ ЗАДАНИЯ
CREATE OR REPLACE PROCEDURE completed_task(task_id INT)
    AS
    $$
    DECLARE
        s CHAR;
    BEGIN
        s := '+';
        EXECUTE format('UPDATE Task SET task_condition = %L WHERE task_id = %L;', s, task_id);
    END;
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE completed_task(task_id INT) TO courier;


--ПРОЦЕДУРА ИЗМЕНЕНИЯ СОСТОЯНИЯ ГОТОВНОСТИ ДОКУМЕНТОВ ДЛЯ МЕТРО
CREATE OR REPLACE PROCEDURE ready_metro(metro_id INT)
    AS
    $$
    BEGIN
        EXECUTE format('UPDATE Metro_station SET metro_station_doc_condition = ''+'' WHERE metro_station_id = %L;', metro_id);
    END;
    $$
    LANGUAGE plpgsql;

GRANT EXECUTE ON PROCEDURE ready_metro(metro_id INT) TO manager;


--Представление готовых к раздаче метро
CREATE OR REPLACE VIEW ready_metro AS
    SELECT metro_station_id, metro_station_name FROM Metro_station
    WHERE metro_station_doc_condition = '+' AND array_length(metro_station_BC_id, 1) IS NOT NULL;

--Просроченные id просроченных задач
CREATE OR REPLACE VIEW bad_task AS
    SELECT task_id FROM Task WHERE task_close_date < now();


SET SESSION AUTHORIZATION bosov123;

CALL create_BC('7ONE',          'Ул. Скобелевская д.4',    '-', 1);
CALL create_BC('Art Residence', 'Ул. Планерная д.32',      '+',     2);
CALL create_BC('Новь',          'Ул. Дмитриевская д.15А', '-', 3);
CALL create_BC('Lost',          'Ул. Саха д.7',    '-', 4);
CALL create_BC('T1',            'Ул. Грибная д.1',  '+',     5);

CALL create_ie('Иван',      'Попов',    79851193331, 1, '402a', '-', '-', NULL, 1);
CALL create_ie('Алексей',   'Рожков',   79851193111, 2, '101', '-', '-', NULL, 2);
CALL create_ie('Ирина',      'Ходулина',    79851193321, 3, '819', '+', '-', NULL, 1);
CALL create_ie('Игорь',      'Пекарев',    79851193123, 4, '2', '+', '-', NULL, 3);
CALL create_ie('Руслан',      'Ариянц',    79191193331, 5, '3', '-', '-', NULL, 4);

CALL create_company('Поль', '100', '-', 6, '-', NULL, 2);
CALL create_company('OMG', '15', '-', 7, '-', 'Заранее подготовить доп. документы', 5);
CALL create_company('Ler', '301', '-', 8, '-', NULL, 5);
CALL create_company('Xtrain', '1002', '+', 9, '-', 'Дверь слева от вывески', 3);
CALL create_company('Solt', '9', '+', 10, '-', 'Сначала звонить Елене', 1);

CALL create_contact_person('Артем',  'Кучин',    79998851112, 1);
CALL create_contact_person('Олег',   'Павшин',   72998888112, 2);
CALL create_contact_person('Слава',  'Левин',    78998334512, 3);
CALL create_contact_person('Макс',   'Черников', 79798851112, 4);
CALL create_contact_person('Джон',   'Хол',      79298825512, 5);
CALL create_contact_person('Егор',   'Микс',     79993001112, 1);

CALL create_task('{1}', '5-5-2023', 3);
CALL create_task('{3}', '5-5-2023', 3);
CALL create_task('{4}', '5-2-2023', 4);
CALL create_task('{5}', '2000-01-01', 4);


SET SESSION AUTHORIZATION postgres;




