# 🛡️ Sentinel IA - Fase 1: Arquiteto Cloud Autônomo

![Arquitetura Sentinel IA - Fase 1](screenshots/arquitetura.png)

## 🏗 Arquitetura do Sistema
![Arquitetura](./assets/architecture.png)

O projeto utiliza uma arquitetura Event-Driven:
1. Imagem é enviada ao **S3**.
2. **Lambda** é disparada automaticamente.
3. **Amazon Bedrock** analisa a imagem em busca de ameaças.
4. Resultados são armazenados e notificados.

O **Sentinel IA** é um motor de automação AIOps que utiliza Inteligência Artificial Generativa para transformar intenções em Infraestrutura como Código (IaC) persistida e segura.

## 🚀 Visão Geral
Este projeto demonstra a integração de ponta a ponta entre **AWS Lambda**, **Amazon Bedrock (Claude 4.5 Haiku)** e **Amazon S3**. O sistema atua como um Engenheiro DevOps Sênior, recebendo instruções em linguagem natural e entregando arquivos `.tf` (Terraform) prontos para deploy.

## 🛠️ Arquitetura e Tecnologias
*   **Linguagem:** Python 3.x (Boto3 SDK)
*   **IA:** Claude 4.5 Haiku via Amazon Bedrock
*   **Storage:** Amazon S3 (com versionamento e proteção de dados)
*   **Segurança:** IAM Policies baseadas no princípio de privilégio mínimo.

## 📋 Passo a Passo de Implementação (PAP)

### 1. Provisionamento do Modelo
*   Acesso ao Amazon Bedrock habilitado para a região `us-east-1`.
*   Subscrição ativa do modelo Anthropic Claude 4.5 Haiku.

### 2. Configuração de Segurança (IAM)
Foram criadas políticas customizadas para garantir que a Lambda possua acesso estrito apenas ao necessário:
*   `PermissaoInvokeBedrock`: Permite a chamada de inferência ao modelo específico.
*   `PermissaoEscritaS3`: Permite o upload de objetos no bucket de destino.

### 3. Desenvolvimento da Lambda
A lógica principal realiza:
1.  Recebimento do prompt via JSON.
2.  Invocação do Bedrock com System Prompt especializado.
3.  Geração de UUID para unicidade de arquivos.
4.  Persistência do artefato no S3 com metadados de `text/plain`.

## 📸 Evidências de Sucesso

### Execução bem-sucedida
![Resultado da Lambda](screenshots/2026-05-02_21-32.png)

### Persistência no S3
![Arquivos no S3](screenshots/2026-05-02_21-31.png)

### Governança e Versionamento
![Versionamento](screenshots/2026-05-02_21-42.png)

## ⚖️ Conclusão da Fase 1
O MVP foi concluído com sucesso, validando a capacidade de orquestração entre IA e serviços de infraestrutura AWS. O sistema está pronto para a Fase 2: Implementação de análise de segurança estática (SAST) nos arquivos gerados.

---

# Sentinel IA - Sistema de Vigilância Inteligente

## 📂 Estrutura do Repositório
*   **/lambda**: Código fonte da função AWS Lambda com integração Claude 3 Haiku.
*   **/docs**: Documentação visual e evidências de testes.
    *   `fase1/`: Logs e prints da infraestrutura inicial.
    *   `fase2/`: Diagrama de arquitetura e prova de conceito (POC) da IA.

## 🚀 Fase 2: Integração de IA Generativa

graph LR
    %% Elementos
    S3[("Amazon S3<br/>(Bucket de Imagens)")]
    Lambda{{"AWS Lambda<br/>(Sentinel Processor)"}}
    Bedrock[["Amazon Bedrock<br/>(Claude 3 Haiku)"]]
    CW[("CloudWatch<br/>(Logs de Alerta)")]

    %% Fluxo de Dados
    S3 -->|1. Evento de Upload| Lambda
    Lambda -->|2. Imagem em Base64| Bedrock
    Bedrock -->|3. Análise IA: ALERTA| Lambda
    Lambda -->|4. Registro da Ocorrência| CW

    %% Estilização
    style S3 fill:#2E7D32,stroke:#fff,color:#fff
    style Lambda fill:#E65100,stroke:#fff,color:#fff
    style Bedrock fill:#1A237E,stroke:#fff,color:#fff
    style CW fill:#546E7A,stroke:#fff,color:#fff
Nesta etapa, o sistema passou a analisar imagens em tempo real.
*   **Trigger**: Upload no S3.
*   **Processamento**: AWS Lambda em Python.
*   **IA**: Anthropic Claude 3 Haiku via Amazon Bedrock.
*   **Resultado**: [Link para o print do Alerta](./docs/fase2/print_cloudwatch.png)

**Desenvolvido por Gustavo - Maio de 2026**
