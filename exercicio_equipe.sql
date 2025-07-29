--Liste o nome completo dos funcionários e o valor total das vendas
--realizadas por cada um, ordenado do maior para o menor valor.
SELECT
    e.first_name || ' ' || e.last_name AS funcionario,
    SUM(od.unit_price * od.quantity * (1 - od.discount)) AS total_vendas
FROM
    employees e
JOIN
    orders o ON e.employee_id = o.employee_id
JOIN
    order_details od ON o.order_id = od.order_id
GROUP BY
    funcionario
ORDER BY
    total_vendas DESC;


--Liste os nomes dos 5 produtos com maior valor total vendido
--(considerando quantidade × preço × desconto)

SELECT
    p.product_name,
    SUM(od.unit_price * od.quantity * (1 - od.discount)) AS total_vendido
FROM
    products p
JOIN
    order_details od ON p.product_id = od.product_id
GROUP BY
    p.product_name
ORDER BY
    total_vendido DESC
LIMIT 5;


--Liste os clientes que fizeram pelo menos um pedido em cada um
--dos anos: 1996, 1997 e 1998

SELECT c.contact_name, c.company_name, c.customer_id
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE EXTRACT(YEAR FROM o.order_date) IN (1996, 1997, 1998)
GROUP BY c.customer_id, c.contact_name, c.company_name
HAVING COUNT(DISTINCT EXTRACT(YEAR FROM o.order_date)) = 3;


--Mostre o nome da categoria que possui o maior número de produtos cadastrados.
SELECT
    c.category_name,
    COUNT(p.product_id) AS total_produtos
FROM
    categories c
JOIN
    products p ON c.category_id = p.category_id
GROUP BY
    c.category_name
ORDER BY
    total_produtos DESC
LIMIT 1;


--Liste o nome dos funcionários que nunca utilizaram a
--transportadora ' Alliance Shippers' para seus pedidos.

SELECT e.first_name || ' ' || e.last_name AS nome_funcionario 
FROM employees e 
WHERE e.employee_id NOT IN (
    SELECT o.employee_id 
    FROM orders o 
    JOIN shippers s ON o.ship_via = s.shipper_id 
    WHERE s.company_name = 'Alliance Shippers'
);

-- EXERCICIO GUIADO POR EQUIPES 2 

-- Listar os clientes que mais compraram, com base em frequência de
--pedidos e valor total gasto.

SELECT
    c.customer_id,
    c.company_name AS cliente,
    COUNT(o.order_id) AS total_pedidos,
    SUM(od.unit_price * od.quantity * (1 - od.discount)) AS valor_total_gasto
FROM
    customers c
JOIN
    orders o ON c.customer_id = o.customer_id
JOIN
    order_details od ON o.order_id = od.order_id
GROUP BY
    c.customer_id, c.company_name
ORDER BY
    valor_total_gasto DESC,
    total_pedidos DESC;

--Detectar produtos com redução de vendas de um ano para o
--seguinte (por exemplo, de 1997 para 1998)

WITH vendas_por_produto AS (
    SELECT
        p.product_id,
        p.product_name,
        EXTRACT(YEAR FROM o.order_date) AS ano,
        SUM(od.quantity) AS total_unidades_vendidas,
        SUM(od.unit_price * od.quantity * (1 - od.discount)) AS total_valor_vendido
    FROM
        products p
    JOIN
        order_details od ON p.product_id = od.product_id
    JOIN
        orders o ON od.order_id = o.order_id
    WHERE
        EXTRACT(YEAR FROM o.order_date) BETWEEN 1997 AND 1998
    GROUP BY
        p.product_id, p.product_name, EXTRACT(YEAR FROM o.order_date)
)

SELECT
    product_id,
    product_name,
    ano,
    total_unidades_vendidas,
    total_valor_vendido
FROM
    vendas_por_produto
WHERE
    (ano = 1997 AND total_unidades_vendidas = (SELECT MIN(total_unidades_vendidas) FROM vendas_por_produto WHERE ano = 1997))
    OR
    (ano = 1998 AND total_unidades_vendidas = (SELECT MIN(total_unidades_vendidas) FROM vendas_por_produto WHERE ano = 1998))
ORDER BY
    ano, total_unidades_vendidas;



