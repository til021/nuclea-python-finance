INSERT INTO users (nome, cpf, rg, birth_day, estado, cidade, bairro,
	            logradouro, cep, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, True);