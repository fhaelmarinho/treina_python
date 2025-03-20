# Gerador e Leitor de QR Code

## Funcionamento

Este software demonstra como gerar e ler QR codes usando Python. Ele utiliza a biblioteca `qrcode` para criar QR codes e a biblioteca `cv2` (OpenCV) para ler e decodificá-los.

### Passos:
1. **Gerar QR Code**:
    - Um QR code é gerado a partir de uma mensagem fornecida (`msg`).
    - O QR code é personalizado com versão específica, tamanho da caixa e borda.
    - A imagem do QR code é salva com uma cor de preenchimento e cor de fundo especificadas.

2. **Ler QR Code**:
    - A imagem do QR code salva é lida usando OpenCV.
    - O QR code é detectado e decodificado para recuperar a mensagem original.
    - A mensagem decodificada é impressa se o QR code for detectado com sucesso; caso contrário, uma mensagem de erro é exibida.

## Objetivos Educacionais

Este projeto tem como objetivo ensinar os seguintes conceitos:
- **Geração de QR Code**: Entender como criar QR codes com configurações personalizadas usando a biblioteca `qrcode`.
- **Processamento de Imagens**: Aprender a ler e processar imagens usando OpenCV.
- **Tratamento de Erros**: Implementar tratamento básico de erros para gerenciar casos em que o QR code não pode ser detectado ou decodificado.
- **Operações com Arquivos**: Salvar e ler arquivos de imagem em Python.
- **Integração de Bibliotecas**: Combinar múltiplas bibliotecas (`qrcode` e `cv2`) para alcançar um objetivo comum.

Ao trabalhar neste projeto, os alunos ganharão experiência prática na geração e leitura de QR codes, que são amplamente utilizados em várias aplicações, como autenticação, compartilhamento de informações e mais.