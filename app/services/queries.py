CREATE_CLIENT = "INSERT INTO clients (phone, code, tag, timezone) VALUES ('{phone}', '{code}', '{tag}', '{timezone}')"
DELETE_CLIENT = "DELETE FROM clients WHERE clients.id = {client_id}"
UPDATE_CLIENT = "UPDATE clients SET phone = '{phone}', code = '{code}', tag = '{tag}', timezone = '{timezone}' WHERE clients.id = {client_id}"

CREATE_MAILING = "INSERT INTO mailing (start_time, message, filter, end_time) VALUES ('{start_time}', '{message}', '{filter}', '{end_time}')"
DELETE_MAILING = "DELETE FROM mailing WHERE mailing.id = {mailing_id}"
UPDATE_MAILING = "UPDATE mailing SET start_time = '{start_time}', message = '{message}', filter = '{filter}', end_time = '{end_time}' WHERE mailing.id = {mailing_id}"