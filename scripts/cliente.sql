CREATE TABLE IF NOT EXISTS public.users 
(
	id SERIAL PRIMARY KEY,
    nome varchar(80) NOT NULL,
    cpf char(14),
    rg varchar(20),
    birth_day date,
    estado char(2),
    cidade varchar(40),
    bairro varchar(40),
    logradouro varchar(40),
    cep char(9),
	status bool
);