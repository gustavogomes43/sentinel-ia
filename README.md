# 🛡️ Sentinel IA — Vigilância Inteligente com IA Generativa (AIOps)

## ⚡ Introdução (Impacto imediato)

E se o seu sistema de segurança **não substituísse pessoas**, mas **direcionasse a atenção delas para o que realmente importa, no momento certo**?

O **Sentinel IA** foi projetado com um objetivo claro:

👉 **IA como suporte à decisão humana — não substituição.**

Enquanto operadores se perdem monitorando dezenas de câmeras, o Sentinel IA atua como um **assistente inteligente**, analisando automaticamente imagens e enviando alertas **diretos, rápidos e acionáveis**.

---

# 🎯 Problema de Negócio

Empresas enfrentam desafios reais em monitoramento:

* 👁️ Sobrecarga de operadores
* ⚠️ Incidentes ignorados ou percebidos tarde
* 🕒 Tempo de resposta elevado
* 💰 Alto custo operacional
* 📉 Baixa eficiência na triagem

---

# 💡 Solução Proposta

O **Sentinel IA** automatiza a análise visual e direciona alertas para quem realmente precisa agir.

## 🧠 Papel da IA no Projeto

O sistema foi desenhado para **trabalhar junto com humanos**:

* 🔔 Alerta o operador responsável
* 📍 Indica o setor/local da ocorrência
* 🚶‍♂️ Direciona a equipe mais próxima
* 🚔 Pode escalar para autoridades

👉 O humano continua no controle — agora com vantagem estratégica

---

# 🎥 Captura de Imagens (Arquitetura Real)

## 🔍 Estratégia adotada: **Snapshot de Vídeo (Frames)**

O sistema **não analisa vídeo diretamente**.
Ele extrai imagens do vídeo em intervalos estratégicos.

## ⚙️ Como funciona

1. Câmeras transmitem vídeo (RTSP/RTMP)
2. Um serviço extrai frames (ex: a cada 2 segundos)
3. Frames são enviados para o S3
4. Pipeline do Sentinel IA realiza a análise

## 🧩 Tecnologias envolvidas

* FFmpeg — captura de frames
* Amazon Kinesis Video Streams — ingestão de vídeo
* Amazon S3 — armazenamento
* AWS Lambda — processamento

## 🎯 Por que essa abordagem?

* 💰 Redução de custo (sem processar vídeo inteiro)
* ⚡ Baixa latência
* 📈 Alta escalabilidade
* 🔧 Simplicidade de integração

👉 **Melhor custo-benefício para sistemas reais**

---

# 🏗️ Arquitetura Geral

Fluxo completo:

1. 🎥 Vídeo capturado
2. 🖼️ Frame extraído
3. 📥 Upload no S3
4. ⚡ Lambda acionada
5. 🧠 IA analisa imagem
6. 📊 Resultado registrado
7. 🔔 (Fase 3) Alerta enviado

---

# 🧠 Tecnologias Utilizadas

| Tecnologia       | Função                   |
| ---------------- | ------------------------ |
| AWS Lambda       | Processamento serverless |
| Amazon S3        | Armazenamento            |
| Amazon Bedrock   | IA generativa            |
| Claude 3/4 Haiku | Análise multimodal       |
| CloudWatch       | Logs                     |
| IAM              | Segurança                |
| Python (Boto3)   | Integração               |

---

# 💰 Custos e Viabilidade

* Modelo sob demanda
* Sem infraestrutura fixa
* Baixo custo inicial
* Escalável

👉 Ideal para MVP e produção

---

# 🚀 FASE 1 — Automação com IA

## 📸 Evidências Explicadas

### `01_s3_bucket_objects`

Valida que os arquivos gerados pela IA foram armazenados com sucesso no S3.

### `02_lambda_overview`

Mostra a configuração da função Lambda e seu estado operacional.

### `03_lambda_test_success`

Confirma que a função executa corretamente sem erros.

### `04_lambda_cloudwatch_logs`

Exibe logs detalhados da execução — essencial para auditoria.

### `05_lambda_python_source`

Código responsável pela integração com IA e geração de arquivos.

### `06_iam_role_permissions`

Demonstra segurança com princípio de menor privilégio.

### `07_bedrock_playground`

Teste direto do modelo de IA antes da integração.

### `08_lambda_test_event`

Simulação de entrada real para testes.

### `09_lambda_execution_result`

Resultado da execução da Lambda.

### `10_terraform_final_code`

Infraestrutura gerada automaticamente pela IA.

### `11_s3_bucket_versioning`

Controle de versões garantindo governança.

---

## 📌 Conclusão Fase 1

Automação de infraestrutura validada com sucesso.

---

# 👁️ FASE 2 — Análise Inteligente

## 📸 Evidências Explicadas

### `arquitetura_sentinel_fase2`

Mostra o fluxo completo do sistema baseado em eventos.

### `cloudwatch`

Registros das análises realizadas pela IA (ALERTA/NORMAL).

### `diagrama_lambda`

Fluxo interno detalhado da Lambda.

### `lambda.py`

Código completo da análise de imagens.

---

## 📈 Resultados

* ⏱️ ~3.8s por análise
* 🎯 Alta precisão
* ⚡ Tempo real

---

## 📌 Conclusão Fase 2

O sistema agora **entende o que está acontecendo nas imagens** e apoia decisões humanas.

---

# 🚧 FASE 3 — Resposta a Incidentes

## 🎯 Objetivo

Transformar análise em ação.

## 🔔 Fluxo de alerta

* IA detecta evento
* Sistema identifica local
* Alerta enviado para:

  * Operador
  * Equipe mais próxima
  * Autoridades

---

# 📊 Benefícios para Empresas

* ↓ Sobrecarga operacional
* ↑ Eficiência
* ↑ Segurança
* ↓ Tempo de resposta

---

# ⚠️ Desafios Enfrentados

* Processamento de imagem
* Integração com IA
* IAM
* Arquitetura escalável

---

# 🔮 Melhorias Futuras

* Dashboard em tempo real
* Banco de eventos
* Integração com câmeras ao vivo
* Edge computing

---

# 🧾 Conclusão Final

O Sentinel IA não substitui pessoas.

👉 Ele **potencializa decisões humanas com velocidade e precisão.**

Transforma vigilância em inteligência.

---

# 👨‍💻 Autor

**Gustavo Gomes**

---

# 🚀 Mensagem Final

Você construiu um sistema que:

👉 Observa
👉 Analisa
👉 Alerta

E principalmente…

👉 **Ajuda pessoas a agir no momento certo**

---

**Status:** 🟢 Fase 2 concluída | 🚧 Fase 3 em andamento
**Ambiente:** AWS Cloud + IA Generativa
