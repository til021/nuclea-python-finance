CREATE TABLE IF NOT EXISTS public.acao
(
    id SERIAL NOT NULL PRIMARY KEY,
    nome character varying(100),
    ticket character varying(10) NOT NULL,
    valor_compra numeric(10, 2) NOT NULL,
	quantidade_compra numeric(5) NOT NULL,
    data_compra date NOT NULL,
    cliente_id integer NOT NULL REFERENCES public.users (id) ON DELETE CASCADE
);
