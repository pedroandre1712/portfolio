

/* Questao 1
Escreva uma consulta SQL que, a partir da tabela film, retorner a lista
classificada, contendo as colunas: id, nome do filme, preco de aluguel e
classificacao
*/
SELECT film_id AS id, title AS nome_do_filme, rental_rate AS preco_de_aluguel,
CASE 
WHEN rental_rate <= 0.99 THEN 'basico'
 	WHEN 0.99<rental_rate AND rental_rate<=2.99 THEN 'essencial'
	WHEN 2.99< rental_rate THEN 'exclusivo'
END AS classificacao 
FROM sakila.film;

/* Questao 2
Escreva uma consulta SQL que utilize o comando CASE WHEN e retorne
a contagem de consumidores ativos e inativos para cada uma das lojas
*/
SELECT store_id AS id_loja, COUNT(active) AS contagem_consumidores,
CASE
    WHEN active=1 and store_id = 1 THEN 'loja1_ativo'
    WHEN active=1 and store_id = 2 THEN 'loja2_ativo'
    WHEN active=0 and store_id = 1 THEN 'loja1_inativo'
    WHEN active=0 and store_id = 2 THEN 'loja2_inativo'
END AS situacao_cliente
FROM sakila.customer
group by situacao_cliente
order by 1;


/* Questao 3
Qual outra estrategia poderia ser utilizada para atingir
o mesmo resultado da pergunta acima?
*/
SELECT 
	store_id, 
	COUNT(store_id) as quantidade_clientes, 
	SUM(active) AS ativos, 
	COUNT(store_id)-SUM(active) AS inativos 
FROM sakila.customer 
GROUP BY store_id;


/* Questao 4
Consultando manualmente o nome da cidade para os 5 primeiros registros da
tabela address, escreva uma consulta SQL que retorne o endereco e o nome da cidade
a qual ele se refere
*/
SELECT address AS endereco,
CASE
    WHEN city_id = 300 THEN 'Lethbridge'
    WHEN city_id = 576 THEN 'Woodridge'
    WHEN city_id = 463 THEN 'Sasebo'
END AS cidade
FROM sakila.address
WHERE sakila.address.address_id < 6;

