sql_pos_calculo = '''
SELECT
	TAB.*

FROM
(
	(SELECT
		A.IDOPORDEMPRODUCAO AS 'CodOP'
		,P.PES_NOME_RAZAO AS 'RazaoSocial'
		,O.descricao AS 'DescOP'
		,OPTF.quantidadeunidadecomercial AS 'QtUnNegComPrevista'
		,CASE OPTF.unidadenegociacaocomercial
			WHEN 1 THEN 'MIL'
			WHEN 2 THEN 'UN'
			WHEN 3 THEN 'JG'
			WHEN 4 THEN 'RL'
			WHEN 5 THEN 'CEN'
			WHEN 6 THEN 'KG'
		END AS 'UnNegComPrevista'
		,ATF.QUANTIDADEUNIDADECOMERCIAL AS 'QtUnNegComRealizada'
		,CASE ATF.UNIDADENEGOCIACAOCOMERCIAL
			WHEN 1 THEN 'MIL'
			WHEN 2 THEN 'UN'
			WHEN 3 THEN 'JG'
			WHEN 4 THEN 'RL'
			WHEN 5 THEN 'CEN'
			WHEN 6 THEN 'KG'
		END AS 'UnNegComRealizada'	
		,IF(T.tipocategoria = 1,'Impressão','Auxiliar') AS 'TipoApuracao'
		,I.IDTARTAREFAREALIZADO AS 'CodItemRealizado'
		,T.descricao AS 'DescItemRealizado'
		,'' AS 'GrupoItem'
		,'' AS 'GrupoPaiItem'
		,SEC_TO_TIME((I.PREV_PREPARACAO + I.PREV_PRODUTIVO) * 60) AS 'TempoQtdePrevisto'
		,I.VLR_ORCADO AS 'VlrOrcado'
		,SEC_TO_TIME((I.REAL_PREPARACAO + I.REAL_PRODUTIVO) * 60) AS 'TempoQtdeRealizado'
		,I.VLR_REALIZADO AS 'VlrRealizado'
		,CC.montagemcarreiras AS 'Carreiras'
		,CARAC.valor AS 'QtPorRolo'
		,A.EMP_ID AS 'Empresa'
		,M.descricao AS 'DescModProd'
		,V.idestitemestoque AS 'CodProduto'
		,OPTF.valortotalbruto AS 'VlrBrutoOP'
	
	FROM
		pcpapuracao A
	
	INNER JOIN
		pcpapuracaoitem I
		ON I.IDPCPAPURACAO = A.ID
	
	INNER JOIN
		pcpapuracaototalrealizado ATF
		ON ATF.IDPCPAPURACAO = A.ID
	
	INNER JOIN
		opordemproducao O
		ON A.IDOPORDEMPRODUCAO = O.id
	
	INNER JOIN
		pessoa P
		ON O.idcliente = P.ID
	
	INNER JOIN
		optotalfinal OPTF
		ON OPTF.idopordemproducao = O.id
	
	INNER JOIN
		tartarefa T
		ON I.IDTARTAREFAREALIZADO = T.id
	
	INNER JOIN
		opcomponente C
		ON C.idopordemproducao = A.IDOPORDEMPRODUCAO
	
	INNER JOIN
		opcompcaracteristica CC
		ON CC.idopcomponente = C.id
	
	LEFT JOIN
		opcaracteristicaproduto CARAC
		ON CARAC.idopordemproducao = A.ID
		AND CARAC.idcaracteristicaproduto = 4
	
	INNER JOIN
		modmodeloproduto M
		ON O.idmodmodeloproduto = M.id
	
	LEFT JOIN
		opvariacao V
		ON V.idopordemproducao = A.IDOPORDEMPRODUCAO
	
	INNER JOIN
		opbaixas OPB
		ON OPB.IDOPORDEMPRODUCAO = A.IDOPORDEMPRODUCAO
	
	WHERE 1=1
	
	)
	UNION ALL
	(
	SELECT
		A.IDOPORDEMPRODUCAO AS 'CodOP'
		,P.PES_NOME_RAZAO AS 'RazaoSocial'
		,O.descricao AS 'DescOP'
		,OPTF.quantidadeunidadecomercial AS 'QtUnNegComPrevista'
		,CASE OPTF.unidadenegociacaocomercial
			WHEN 1 THEN 'MIL'
			WHEN 2 THEN 'UN'
			WHEN 3 THEN 'JG'
			WHEN 4 THEN 'RL'
			WHEN 5 THEN 'CEN'
			WHEN 6 THEN 'KG'
		END AS 'UnNegComPrevista'
		,ATF.QUANTIDADEUNIDADECOMERCIAL AS 'QtUnNegComRealizada'
		,CASE ATF.UNIDADENEGOCIACAOCOMERCIAL
			WHEN 1 THEN 'MIL'
			WHEN 2 THEN 'UN'
			WHEN 3 THEN 'JG'
			WHEN 4 THEN 'RL'
			WHEN 5 THEN 'CEN'
			WHEN 6 THEN 'KG'
		END AS 'UnNegComRealizada'	
		,'Material' AS 'TipoApuracao'
		,I.IDESTITEMESTOQUEREALIZADO AS 'CodItemRealizado'
		,E.descricao AS 'DescItemRealizado'
		,G1.descricao AS 'GrupoItem'
		,G2.descricao AS 'GrupoPaiItem'	
		,I.QTD_ORCADO AS 'TempoQtdePrevisto'
		,I.VLR_ORCADO AS 'VlrOrcado'
		,I.QTD_REALIZADO AS 'TempoQtdeRealizado'
		,I.VLR_REALIZADO AS 'VlrRealizado'
		,CC.montagemcarreiras AS 'Carreiras'
		,CARAC.valor AS 'QtPorRolo'
		,A.EMP_ID AS 'Empresa'
		,M.descricao AS 'DescModProd'
		,V.idestitemestoque AS 'CodProduto'
		,OPTF.valortotalbruto AS 'VlrBrutoOP'
	
	FROM
		pcpapuracao A
	
	INNER JOIN
		pcpapuracaoitem I
		ON I.IDPCPAPURACAO = A.ID
	
	INNER JOIN
		pcpapuracaototalrealizado ATF
		ON ATF.IDPCPAPURACAO = A.ID
	
	INNER JOIN
		opordemproducao O
		ON A.IDOPORDEMPRODUCAO = O.id
	
	INNER JOIN
		pessoa P
		ON O.idcliente = P.ID
	
	INNER JOIN
		optotalfinal OPTF
		ON OPTF.idopordemproducao = O.id
	
	INNER JOIN
		estitemestoque E
		ON I.IDESTITEMESTOQUEREALIZADO = E.id
	
	INNER JOIN
		grupoitemestoque G1
		ON E.idgrupoitemestoque = G1.id
	
	LEFT JOIN
		grupoitemestoque G2
		ON G1.idgrupoitemestoque = G2.id
	
	INNER JOIN
		opcomponente C
		ON C.idopordemproducao = A.IDOPORDEMPRODUCAO
	
	INNER JOIN
		opcompcaracteristica CC
		ON CC.idopcomponente = C.id
	
	LEFT JOIN
		opcaracteristicaproduto CARAC
		ON CARAC.idopordemproducao = A.ID
		AND CARAC.idcaracteristicaproduto = 4
	
	INNER JOIN
		modmodeloproduto M
		ON O.idmodmodeloproduto = M.id
	
	LEFT JOIN
		opvariacao V
		ON V.idopordemproducao = A.IDOPORDEMPRODUCAO
	
	INNER JOIN
		opbaixas OPB
		ON OPB.IDOPORDEMPRODUCAO = A.IDOPORDEMPRODUCAO
	
	WHERE 1=1
	)

) AS TAB

ORDER BY
	TAB.CodOP
	,TAB.TipoApuracao
'''

sql_nome_operadores = '''
SELECT 
		 AA.DATAHORAINICIAL AS Data,
			AA.IDOP AS CodigoOP,
			AA.IDEP AS CodigoEquipamento,
			AA.descricao AS Impressora,
			AA.NOME AS Impressor,
			B.descricao AS Revisora,
			B.NOME AS Revisor,
			C.descricao AS Batedora,
			C.NOME AS Batida
FROM

(

SELECT

A.DATAHORAINICIAL,
P.IDOPORDEMPRODUCAO AS IDOP,
OP.NOME,
E.ID AS IDEP,
E.DESCRICAO


FROM 
pcpapontamento A

INNER JOIN
	pcpprocessos P
	ON A.EMP_ID = P.EMP_ID	
	AND A.CODIGOTRABALHO = P.CODIGOTRABALHO
	AND A.CODIGOPROCESSO =P.CODIGO

LEFT JOIN 
	EQUIPAMENTO E
	ON P.IDEQUIPAMENTO = E.ID
	
LEFT JOIN 
 operador OP
 ON OP.ID = A.IDOPERADOR
 
WHERE (P.TIPOTAREFA = 'IMPRESSAO' OR P.TIPOTAREFA != 'IMPRESSAO')
AND NOT P.IDEQUIPAMENTO IN (9,10)

 

) AS AA

LEFT JOIN (

SELECT

A.DATAHORAINICIAL,
P.IDOPORDEMPRODUCAO AS IDOP,
OP.NOME,
E.ID AS IDEP,
E.DESCRICAO

FROM 
pcpapontamento A

INNER JOIN
	pcpprocessos P
	ON A.EMP_ID = P.EMP_ID	
	AND A.CODIGOTRABALHO = P.CODIGOTRABALHO
	AND A.CODIGOPROCESSO =P.CODIGO

LEFT JOIN 
	EQUIPAMENTO E
	ON P.IDEQUIPAMENTO = E.ID
	
LEFT JOIN 
 operador OP
 ON OP.ID = A.IDOPERADOR
 
WHERE P.TIPOTAREFA = 'AUXILIARCOMPONENTE'
AND NOT P.IDEQUIPAMENTO IN (9,10)
  

) AS B
ON AA.IDOP = B.IDOP


LEFT JOIN (

SELECT

A.DATAHORAINICIAL,
P.IDOPORDEMPRODUCAO AS IDOP,
OP.NOME,
E.ID AS IDEP,
E.DESCRICAO

FROM 
pcpapontamento A

INNER JOIN
	pcpprocessos P
	ON A.EMP_ID = P.EMP_ID	
	AND A.CODIGOTRABALHO = P.CODIGOTRABALHO
	AND A.CODIGOPROCESSO =P.CODIGO

LEFT JOIN 
	EQUIPAMENTO E
	ON P.IDEQUIPAMENTO = E.ID
	
LEFT JOIN 
 operador OP
 ON OP.ID = A.IDOPERADOR
 
WHERE P.IDEQUIPAMENTO IN (9,10)
 

) AS C

ON AA.IDOP = C.IDOP
WHERE 1=1
GROUP BY AA.IDOP
ORDER BY AA.DATAHORAINICIAL DESC 
'''