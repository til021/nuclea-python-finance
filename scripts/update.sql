UPDATE users
SET nome = %s,
	cpf = %s,
	rg = %s,
	birth_day = %s,
	estado = %s,
	cidade = %s,
	bairro = %s,
	logradouro = %s,
	cep = %s
WHERE id = %s;
"""