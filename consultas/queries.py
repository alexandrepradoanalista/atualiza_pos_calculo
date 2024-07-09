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
		ON CARAC.idopordemproducao = A.IDOPORDEMPRODUCAO
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
		ON CARAC.idopordemproducao = A.IDOPORDEMPRODUCAO
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

sql_faturamento = '''
SELECT
	DC.EMP_ID AS 'Empresa'
	,DC.SERIENF AS 'SerieNF'
	,DC.NUMERONF AS 'NumeroNF'
	,DC.DATAEMISSAO AS 'DataNF'
	,DC.IDPESSOA AS 'idCLiente'
	,P.PES_NOME_RAZAO AS 'Cliente'
	,DC.IDVENDEDOR AS 'idVendedor'
	,VEN.PES_NOME_RAZAO AS 'Vendedor'
	,DIC.PERCCOMISSAO AS 'PercComissao'
	,DI.IDESTITEMESTOQUE AS 'CodItem'
	,DI.DESCRICAOITEM AS 'DescItem'
	,E.idgrupoitemestoque AS 'idGrupo'
	,G.descricao AS 'DescGrupo'
	,DI.QUANTIDADE AS 'Quantidade'
	,CASE DI.UNIDADEMEDIDA
		WHEN 1 THEN 'M2'
		WHEN 2 THEN 'KG'
		WHEN 3 THEN 'FL'
		WHEN 4 THEN 'ML'
		WHEN 5 THEN 'BO'
		WHEN 6 THEN 'RM'
		WHEN 7 THEN 'PC'
		WHEN 8 THEN 'UN'
		WHEN 9 THEN 'BL'
		WHEN 10 THEN 'MIL'
		WHEN 11 THEN 'CN'
		WHEN 12 THEN 'MT'
		WHEN 13 THEN 'HR'
		WHEN 14 THEN 'G'
		WHEN 15 THEN 'CM2'
		WHEN 16 THEN 'FOR'
		WHEN 17 THEN 'LIV'
		WHEN 18 THEN 'MT3'
		WHEN 19 THEN 'F'
		WHEN 20 THEN 'L'
		WHEN 21 THEN 'CML'
		WHEN 22 THEN 'CX'
		WHEN 23 THEN 'JG'
		WHEN 24 THEN 'MM'
		WHEN 25 THEN 'MTT'
		WHEN 26 THEN 'PCT'
		WHEN 27 THEN 'RL'
		WHEN 28 THEN 'MH/JG'
		WHEN 29 THEN 'GL'
		WHEN 30 THEN 'GG'
		WHEN 31 THEN 'BD'
		WHEN 32 THEN 'FD'
		WHEN 33 THEN 'TON'
		WHEN 34 THEN 'CM'
		WHEN 35 THEN 'KM'
		WHEN 36 THEN 'PAR'
	END AS 'Unidade'
	,(
		SELECT
			SI2.quantidadeimpressaom2 / I2.quantidade
		FROM
			orcorcamento O2
		INNER JOIN
			orcitem I2
			ON I2.idorcorcamento = O2.id
		INNER JOIN
			orccomponente C2
			ON C2.iditem = I2.id
		INNER JOIN
			orccompsubsimpressaoprincipal S2
			ON S2.idorccomponente = C2.id
		INNER JOIN
			orccompsubstratoimpprincipalcalc SI2
			ON SI2.idorccompsubsimpressaoprincipal = S2.id
		INNER JOIN
			orcitemvariacao V2
			ON V2.idorcitem = I2.id
		WHERE 1=1
			AND V2.idestitemestoque = DI.IDESTITEMESTOQUE
		GROUP BY
			V2.idestitemestoque	
	) * DI.QUANTIDADE / IFNULL(IC.fatorconversao,1) AS 'm2Total'
	,DIC.VALORLIQUIDO + DIC.BASECALCULOIPI * (DIC.PERCIPI / 100) AS 'ValorLiquido'
	,DI.CFOP AS 'CFOP'
	,EN.END_CIDADE AS 'Cidade'
	,EN.END_UF AS 'UF'
	,OCSE.idgrupoitemestoque AS 'idGrupoSubstrato'
	,OCSEG.descricao AS 'descGrupoSubstrato'
	,OCS.idsubstrato AS 'idSubstrato'
	,OCSE.descricao AS 'descSubstrato'
	,OCF.idfaca AS 'idFaca'
	,OI.idorcorcamento AS 'idOrc'
	,OCFE.codigoreferencia AS 'refFaca'
	,OCFE.descricao AS 'descFaca'
	,PV.SERIENF AS 'SeriePV'
	,PV.NUMERONF AS 'NumPV'
	,PVIE.QUANTIDADEENTREGA AS 'QtdePrevista'
	,PVIE.DATAENTREGAPEDIDO AS 'DataPrevista'
	,DIC.BASECALCULOICMS AS 'BaseCalculoICMS'
	,DIC.PERCICMS AS 'PercICMS'
	,DIC.BASECALCULOIPI AS 'BaseCalculoIPI'
	,DIC.PERCIPI AS 'PercIPI'
	,DIC.BASECALCULOPIS AS 'BaseCalcloPIS'
	,DIC.PERCPIS
	,DIC.BASECALCULOCOFINS AS 'BaseCalculoCOFINS'
	,DIC.PERCCOFINS AS 'PercCofins'
	,C.IDATIVIDADE AS 'CodAtividade'
	,A.ATI_DESCRICAO AS 'DescAtividade'
	,F.fatorconversao AS 'Fator'
	,V.valormedio AS 'ValorMedio'
	,OPV.idopordemproducao AS 'CodOP'
#	,DIC.BASECALCULOIPI * (DIC.PERCIPI / 100) AS 'ValorIPI'

FROM
	documentocabecalho DC

INNER JOIN
	documentoitem DI
	ON DC.EMP_ID = DI.EMP_ID
	AND DC.CLASSIFICACAO = DI.CLASSIFICACAO
	AND DC.DOC_ID = DI.DOC_ID

INNER JOIN
	documentoitemcalculo DIC
	ON DI.EMP_ID = DIC.EMP_ID
	AND DI.CLASSIFICACAO = DIC.CLASSIFICACAO
	AND DI.DOC_ID = DIC.DOC_ID
	AND DI.SEQUENCIALITEM = DIC.SEQUENCIALITEM

LEFT JOIN
	orcitem OI
	ON DI.IDORCITEM = OI.id

LEFT JOIN
	estitemconversao IC
	ON DI.IDESTITEMESTOQUE = IC.idestitemestoque

INNER JOIN
	estitemestoque E
	ON E.id = DI.IDESTITEMESTOQUE

INNER JOIN
	estitemvalores V
	ON E.id = V.idestitemestoque

INNER JOIN
	grupoitemestoque G
	ON G.id = E.idgrupoitemestoque

LEFT JOIN
	estitemconversao F
	ON F.idestitemestoque = E.id

INNER JOIN
	pessoa P
	ON DC.IDPESSOA = P.ID

INNER JOIN
	pessoa VEN
	ON DC.IDVENDEDOR = VEN.ID

INNER JOIN
	endereco EN
	ON DC.IDPESSOA = EN.IDPESSOA
	AND DC.IDENDERECO = EN.ID

LEFT JOIN
	orccomponente OC
	ON OC.iditem = OI.id

LEFT JOIN
	orccompsubsimpressaoprincipal OCS
	ON OCS.idorccomponente = OC.id

LEFT JOIN
	estitemestoque OCSE
	ON OCSE.id = OCS.idsubstrato

LEFT JOIN
	grupoitemestoque OCSEG
	ON OCSEG.id = OCSE.idgrupoitemestoque

LEFT JOIN
	orccompfacaprincipal OCF
	ON OCF.idorccomponente = OC.id

LEFT JOIN
	estitemestoque OCFE
	ON OCFE.id = OCF.idfaca

LEFT JOIN
	documentoitementregas PVIE
	ON PVIE.EMP_ID = DI.EMP_ID
	AND PVIE.CLASSIFICACAO = DI.CLASSPEDCOMPRA
	AND PVIE.DOC_ID = DI.CODPEDCOMPRA
	AND PVIE.SEQUENCIALITEM = DI.SEQPEDCOMPRA
	AND PVIE.IDENTREGAS = DI.IDENTREGAPEDCOMPRA

LEFT JOIN
	documentoitem PVI
	ON PVIE.EMP_ID = PVI.EMP_ID
	AND PVIE.CLASSIFICACAO = PVI.CLASSIFICACAO
	AND PVIE.DOC_ID = PVI.DOC_ID
	AND PVIE.SEQUENCIALITEM = PVI.SEQUENCIALITEM

LEFT JOIN
	documentocabecalho PV
	ON PV.EMP_ID = PVI.EMP_ID
	AND PV.CLASSIFICACAO = PVI.CLASSIFICACAO
	AND PV.DOC_ID = PVI.DOC_ID

LEFT JOIN
	oppedidos OPP
	ON OPP.idempresa = PVI.EMP_ID
	AND OPP.classificacao = PVI.CLASSIFICACAO
	AND OPP.doc_id = PVI.DOC_ID
	AND OPP.sequencialitem = PVI.SEQUENCIALITEM

LEFT JOIN
	opvariacao OPV
	ON OPP.idopvariacao = OPV.id

LEFT JOIN
	cliente C
	ON C.IDPESSOA = P.ID

LEFT JOIN
	atividade A
	ON C.IDATIVIDADE = A.ID

WHERE 1=1
	AND DC.CLASSIFICACAO = 0
	AND DC.CANCELADA = 'N'
	AND DI.GEROUFATURAMENTO = 'S'
	AND DI.CFOP IN ('0.000','5.101','5.102','5.118','5.119','5.122','5.123','5.405','5.551'
		           ,'5.553','5.933','5.949','6.101','6.102','6.107','6.108','6.109','6.110'
		           ,'6.118','6.119','6.122','6.123','6.404','6.551','6.933')

GROUP BY
	DC.EMP_ID
	,DC.CLASSIFICACAO
	,DC.DOC_ID
	,DI.SEQUENCIALITEM
'''

sql_faturamento_novo = """
SELECT
	DC.EMP_ID AS 'Empresa'
	,DC.SERIENF AS 'SerieNF'
	,DC.NUMERONF AS 'NumeroNF'
	,DC.DATAEMISSAO AS 'DataNF'
	,DC.IDPESSOA AS 'idCLiente'
	,P.PES_NOME_RAZAO AS 'Cliente'
	,DC.IDVENDEDOR AS 'idVendedor'
	,VEN.PES_NOME_RAZAO AS 'Vendedor'
	,DIC.PERCCOMISSAO AS 'PercComissao'
	,DI.IDESTITEMESTOQUE AS 'CodItem'
	,DI.DESCRICAOITEM AS 'DescItem'
	,E.idgrupoitemestoque AS 'idGrupo'
	,G.descricao AS 'DescGrupo'
	,DI.QUANTIDADE AS 'Quantidade'
	,CASE DI.UNIDADEMEDIDA
		WHEN 1 THEN 'M2'
		WHEN 2 THEN 'KG'
		WHEN 3 THEN 'FL'
		WHEN 4 THEN 'ML'
		WHEN 5 THEN 'BO'
		WHEN 6 THEN 'RM'
		WHEN 7 THEN 'PC'
		WHEN 8 THEN 'UN'
		WHEN 9 THEN 'BL'
		WHEN 10 THEN 'MIL'
		WHEN 11 THEN 'CN'
		WHEN 12 THEN 'MT'
		WHEN 13 THEN 'HR'
		WHEN 14 THEN 'G'
		WHEN 15 THEN 'CM2'
		WHEN 16 THEN 'FOR'
		WHEN 17 THEN 'LIV'
		WHEN 18 THEN 'MT3'
		WHEN 19 THEN 'F'
		WHEN 20 THEN 'L'
		WHEN 21 THEN 'CML'
		WHEN 22 THEN 'CX'
		WHEN 23 THEN 'JG'
		WHEN 24 THEN 'MM'
		WHEN 25 THEN 'MTT'
		WHEN 26 THEN 'PCT'
		WHEN 27 THEN 'RL'
		WHEN 28 THEN 'MH/JG'
		WHEN 29 THEN 'GL'
		WHEN 30 THEN 'GG'
		WHEN 31 THEN 'BD'
		WHEN 32 THEN 'FD'
		WHEN 33 THEN 'TON'
		WHEN 34 THEN 'CM'
		WHEN 35 THEN 'KM'
		WHEN 36 THEN 'PAR'
	END AS 'Unidade'
	,(
		SELECT
			SI2.quantidadeimpressaom2 / I2.quantidade
		FROM
			orcorcamento O2
		INNER JOIN
			orcitem I2
			ON I2.idorcorcamento = O2.id
		INNER JOIN
			orccomponente C2
			ON C2.iditem = I2.id
		INNER JOIN
			orccompsubsimpressaoprincipal S2
			ON S2.idorccomponente = C2.id
		INNER JOIN
			orccompsubstratoimpprincipalcalc SI2
			ON SI2.idorccompsubsimpressaoprincipal = S2.id
		INNER JOIN
			orcitemvariacao V2
			ON V2.idorcitem = I2.id
		WHERE 1=1
			AND V2.idestitemestoque = DI.IDESTITEMESTOQUE
		GROUP BY
			V2.idestitemestoque	
	) * DI.QUANTIDADE / IFNULL(IC.fatorconversao,1) AS 'm2Total'
	,DIC.VALORLIQUIDO + DIC.BASECALCULOIPI * (DIC.PERCIPI / 100) AS 'ValorLiquido'
	,DI.CFOP AS 'CFOP'
	,EN.END_CIDADE AS 'Cidade'
	,EN.END_UF AS 'UF'
	,OCSE.idgrupoitemestoque AS 'idGrupoSubstrato'
	,OCSEG.descricao AS 'descGrupoSubstrato'
	,OCS.idsubstrato AS 'idSubstrato'
	,OCSE.descricao AS 'descSubstrato'
	,OCF.idfaca AS 'idFaca'
	,OI.idorcorcamento AS 'idOrc'
	,OCFE.codigoreferencia AS 'refFaca'
	,OCFE.descricao AS 'descFaca'
	,PV.SERIENF AS 'SeriePV'
	,PV.NUMERONF AS 'NumPV'
	,PVIE.QUANTIDADEENTREGA AS 'QtdePrevista'
	,PVIE.DATAENTREGAPEDIDO AS 'DataPrevista'
	,DIC.BASECALCULOICMS AS 'BaseCalculoICMS'
	,DIC.PERCICMS AS 'PercICMS'
	,DIC.BASECALCULOIPI AS 'BaseCalculoIPI'
	,DIC.PERCIPI AS 'PercIPI'
	,DIC.BASECALCULOPIS AS 'BaseCalcloPIS'
	,DIC.PERCPIS
	,DIC.BASECALCULOCOFINS AS 'BaseCalculoCOFINS'
	,DIC.PERCCOFINS AS 'PercCofins'
	,C.IDATIVIDADE AS 'CodAtividade'
	,A.ATI_DESCRICAO AS 'DescAtividade'
	,F.fatorconversao AS 'Fator'
	,V.valormedio AS 'ValorMedio'
#	,DIC.BASECALCULOIPI * (DIC.PERCIPI / 100) AS 'ValorIPI'

FROM
	documentocabecalho DC

INNER JOIN
	documentoitem DI
	ON DC.EMP_ID = DI.EMP_ID
	AND DC.CLASSIFICACAO = DI.CLASSIFICACAO
	AND DC.DOC_ID = DI.DOC_ID

INNER JOIN
	documentoitemcalculo DIC
	ON DI.EMP_ID = DIC.EMP_ID
	AND DI.CLASSIFICACAO = DIC.CLASSIFICACAO
	AND DI.DOC_ID = DIC.DOC_ID
	AND DI.SEQUENCIALITEM = DIC.SEQUENCIALITEM

LEFT JOIN
	orcitem OI
	ON DI.IDORCITEM = OI.id

LEFT JOIN
	estitemconversao IC
	ON DI.IDESTITEMESTOQUE = IC.idestitemestoque

INNER JOIN
	estitemestoque E
	ON E.id = DI.IDESTITEMESTOQUE

INNER JOIN
	estitemvalores V
	ON E.id = V.idestitemestoque

INNER JOIN
	grupoitemestoque G
	ON G.id = E.idgrupoitemestoque

LEFT JOIN
	estitemconversao F
	ON F.idestitemestoque = E.id

INNER JOIN
	pessoa P
	ON DC.IDPESSOA = P.ID

INNER JOIN
	pessoa VEN
	ON DC.IDVENDEDOR = VEN.ID

INNER JOIN
	endereco EN
	ON DC.IDPESSOA = EN.IDPESSOA
	AND DC.IDENDERECO = EN.ID

LEFT JOIN
	orccomponente OC
	ON OC.iditem = OI.id

LEFT JOIN
	orccompsubsimpressaoprincipal OCS
	ON OCS.idorccomponente = OC.id

LEFT JOIN
	estitemestoque OCSE
	ON OCSE.id = OCS.idsubstrato

LEFT JOIN
	grupoitemestoque OCSEG
	ON OCSEG.id = OCSE.idgrupoitemestoque

LEFT JOIN
	orccompfacaprincipal OCF
	ON OCF.idorccomponente = OC.id

LEFT JOIN
	estitemestoque OCFE
	ON OCFE.id = OCF.idfaca

LEFT JOIN
	documentoitementregas PVIE
	ON PVIE.EMP_ID = DI.EMP_ID
	AND PVIE.CLASSIFICACAO = DI.CLASSPEDCOMPRA
	AND PVIE.DOC_ID = DI.CODPEDCOMPRA
	AND PVIE.SEQUENCIALITEM = DI.SEQPEDCOMPRA
	AND PVIE.IDENTREGAS = DI.IDENTREGAPEDCOMPRA

LEFT JOIN
	documentoitem PVI
	ON PVIE.EMP_ID = PVI.EMP_ID
	AND PVIE.CLASSIFICACAO = PVI.CLASSIFICACAO
	AND PVIE.DOC_ID = PVI.DOC_ID
	AND PVIE.SEQUENCIALITEM = PVI.SEQUENCIALITEM

LEFT JOIN
	documentocabecalho PV
	ON PV.EMP_ID = PVI.EMP_ID
	AND PV.CLASSIFICACAO = PVI.CLASSIFICACAO
	AND PV.DOC_ID = PVI.DOC_ID

LEFT JOIN
	cliente C
	ON C.IDPESSOA = P.ID

LEFT JOIN
	atividade A
	ON C.IDATIVIDADE = A.ID

WHERE 1=1
	AND DC.CLASSIFICACAO = 0
	AND DC.CANCELADA = 'N'
	AND DI.GEROUFATURAMENTO = 'S'
	AND DI.CFOP IN ('0.000','5.101','5.102','5.118','5.119','5.122','5.123','5.405','5.551'
		           ,'5.553','5.933','5.949','6.101','6.102','6.107','6.108','6.109','6.110'
		           ,'6.118','6.119','6.122','6.123','6.404','6.551','6.933')

GROUP BY
	DC.EMP_ID
	,DC.CLASSIFICACAO
	,DC.DOC_ID
	,DI.SEQUENCIALITEM
	
ORDER BY 
	DC.DATAEMISSAO
	
	"""

sql_pedidos = '''
SELECT
	DC.EMP_ID AS 'CodEmpresa'
	,DC.SERIENF AS 'SeriePedido'
	,DC.NUMERONF AS 'NumeroPedido'
	,DC.DATAEMISSAO AS 'DataEmissao'
	,DC.IDPESSOA AS 'CodCliente'
	,P.PES_NOME_RAZAO AS 'NomeCliente'
	,DC.IDVENDEDOR AS 'CodVendedor'
	,V.PES_NOME_RAZAO AS 'NomeVendedor'
	,DI.IDESTITEMESTOQUE AS 'CodProduto'
	,DI.DESCRICAOITEM AS 'DescProduto'
	,DI.QUANTIDADE AS 'Quantidade'
	,DI.VALORUNITARIO AS 'ValorUnitario'
	,CASE DI.UNIDADEMEDIDA
		WHEN 1 THEN 'M2'
		WHEN 2 THEN 'KG'
		WHEN 3 THEN 'FL'
		WHEN 4 THEN 'ML'
		WHEN 5 THEN 'BO'
		WHEN 6 THEN 'RM'
		WHEN 7 THEN 'PC'
		WHEN 8 THEN 'UN'
		WHEN 9 THEN 'BL'
		WHEN 10 THEN 'MIL'
		WHEN 11 THEN 'CN'
		WHEN 12 THEN 'MT'
		WHEN 13 THEN 'HR'
		WHEN 14 THEN 'G'
		WHEN 15 THEN 'CM2'
		WHEN 16 THEN 'FOR'
		WHEN 17 THEN 'LIV'
		WHEN 18 THEN 'MT3'
		WHEN 19 THEN 'F'
		WHEN 20 THEN 'L'
		WHEN 21 THEN 'CML'
		WHEN 22 THEN 'CX'
		WHEN 23 THEN 'JG'
		WHEN 24 THEN 'MM'
		WHEN 25 THEN 'MTT'
		WHEN 26 THEN 'PCT'
		WHEN 27 THEN 'RL'
		WHEN 28 THEN 'MH/JG'
		WHEN 29 THEN 'GL'
		WHEN 30 THEN 'GG'
		WHEN 31 THEN 'BD'
		WHEN 32 THEN 'FD'
		WHEN 33 THEN 'TON'
		WHEN 34 THEN 'CM'
		WHEN 35 THEN 'KM'
		WHEN 36 THEN 'PAR'
	END AS 'Unidade'
	,E.idgrupoitemestoque AS 'CodGrupoItem'
	,G.descricao AS 'DescGrupoItem'
	,DIC.VALORBRUTO AS 'ValorBruto'
	,DIC.VALORLIQUIDO AS 'ValorLiquido'
	,DIC.VALORFATURADO AS 'ValorFaturado'
	,DIC.PERCICMS AS 'PercICMS'
	,DIC.VALORICMS AS 'ValorICMS'
	,DIC.PERCIPI AS 'PercIPI'
	,DIC.VALORIPI AS 'ValorIPI'
	,DIC.VALORCOMISSAO AS 'ValorComissao'
	,FP.FOP_DESCRICAO AS 'FormaPagto'
	,MIN(DIE.DATAENTREGAPEDIDO) AS 'DataEntrega'

FROM
	documentocabecalho DC

INNER JOIN
	documentoitem DI
	ON DC.EMP_ID = DI.EMP_ID
	AND DC.CLASSIFICACAO = DI.CLASSIFICACAO
	AND DC.DOC_ID = DI.DOC_ID

INNER JOIN
	documentoitemcalculo DIC
	ON DI.EMP_ID = DIC.EMP_ID
	AND DI.CLASSIFICACAO = DIC.CLASSIFICACAO
	AND DI.DOC_ID = DIC.DOC_ID
	AND DI.SEQUENCIALITEM = DIC.SEQUENCIALITEM

INNER JOIN
	documentoitementregas DIE
	ON DI.EMP_ID = DIE.EMP_ID
	AND DI.CLASSIFICACAO = DIE.CLASSIFICACAO
	AND DI.DOC_ID = DIE.DOC_ID
	AND DI.SEQUENCIALITEM = DIE.SEQUENCIALITEM

INNER JOIN
	pessoa P
	ON DC.IDPESSOA = P.ID

INNER JOIN
	pessoa V
	ON DC.IDVENDEDOR = V.ID

INNER JOIN
	formapagto FP
	ON DC.IDFORMAPAGTO = FP.ID

INNER JOIN
	estitemestoque E
	ON DI.IDESTITEMESTOQUE = E.id

INNER JOIN
	grupoitemestoque G
	ON E.idgrupoitemestoque = G.id

WHERE 1=1
	AND DC.CLASSIFICACAO = 2
	AND DC.CANCELADA = 'N'
	AND DIC.VALORFATURADO > 0
	AND DC.DATAEMISSAO <= NOW()

GROUP BY
	DI.EMP_ID
	,DI.CLASSIFICACAO
	,DI.DOC_ID
	,DI.SEQUENCIALITEM
	
ORDER BY
	DC.DATAEMISSAO
	
'''

sql_produtividade = '''
SELECT
	P.IDEQUIPAMENTO AS ID
	,P.DESCRICAOEQUIPAMENTO AS 'Equipamento'	
	,A.DATAHORAINICIAL AS 'Inicio'
	,A.DATAHORAFINAL AS 'Fim'
	,T.IDOPORDEMPRODUCAO AS 'OP'
	,P.DESCRICAOTARTAREFA AS 'tarefa'
	,P.TIPOTAREFA AS 'tipoTarefa'
	,V.idestitemestoque AS 'codItem'
	,E.descricao AS 'Item'
	,P.QUANTIDADE AS 'Quantidade'
	,A.QTMETROLINEAR AS 'QuantidadeMetrosLineares'
	,OC.DESCRICAO AS 'Ocorrencias'
	,OP.NOME	AS 'Operador'
	,OPCI.tiragemtotalcalc AS 'totalmetroslinearesprevisto'	
	,O.quantidade AS 'QuantidadePrevista'
	,OPC.montagemcarreiras AS 'Carreiras'
    
FROM
	pcptrabalhos T
	
INNER JOIN
	pcpprocessos P
	ON T.EMP_ID = P.EMP_ID
	AND T.CODIGO = P.CODIGOTRABALHO

INNER JOIN
	pcpapontamento A
	ON P.EMP_ID = A.EMP_ID
	AND P.CODIGOTRABALHO = A.CODIGOTRABALHO 
	AND P.CODIGO = A.CODIGOPROCESSO

INNER JOIN
	opordemproducao O
	ON T.IDOPORDEMPRODUCAO = O.id

INNER JOIN 
	ocorrencia OC
	ON A.IDOCORRENCIA = OC.ID
	
INNER JOIN 
	operador OP
	ON A.IDOPERADOR = OP.ID

LEFT JOIN
	opvariacao V
	ON V.idopordemproducao = O.id

LEFT JOIN
	estitemestoque E
	ON V.idestitemestoque = E.id

INNER JOIN 
	opcompcaracteristica OPC
	ON P.IDOPCOMPONENTE = OPC.idopcomponente
	
INNER JOIN 
	opcompcaracteristicaimpressao OPCI
	ON OPC.id = OPCI.id


LEFT JOIN 
	opcaracteristicaproduto OPCP
	ON O.id = OPCP.idopordemproducao

WHERE 1=1
	AND A.DATAHORAINICIAL <= NOW()

GROUP BY
	A.DATAHORAINICIAL,
	OC.DESCRICAO

ORDER BY 
	A.DATAHORAINICIAL;

'''