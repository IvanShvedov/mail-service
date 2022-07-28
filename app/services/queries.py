CREATE_CLIENT = "INSERT INTO clients (phone, code, tag, timezone) VALUES ('{phone}', '{code}', '{tag}', '{timezone}')"
DELETE_CLIENT = "DELETE FROM clients WHERE clients.id = {client_id}"
UPDATE_CLIENT = "UPDATE clients SET phone = '{phone}', code = '{code}', tag = '{tag}', timezone = '{timezone}' WHERE clients.id = {client_id}"