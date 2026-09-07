# MEC Livros para KOReader

Plugin não-oficial do [KOReader](https://koreader.rocks/) para a plataforma
**MEC Livros** (<https://meclivros.mec.gov.br/>). Permite buscar, emprestar,
renovar e devolver livros, além de baixar obras de domínio público, para ler
diretamente no KOReader.

> ⚠️ **Aviso.** Projeto independente, sem vínculo com o MEC. Use apenas com a
> sua própria conta e token. O plugin baixa o conteúdo de livros emprestados ou
> de obras que a própria plataforma marca como domínio público, reconstruindo um
> EPUB local a partir do manifesto de leitura. Respeite os termos de uso do
> serviço e o modelo de empréstimo (o acesso é pensado para durar enquanto o
> empréstimo estiver válido).

## Como funciona

A plataforma não oferece download de EPUB completo. A leitura acontece sobre um
*Web Publication Manifest* (perfil EPUB do Readium), cujos recursos são servidos
de forma autenticada por `/epub-proxy/webpub/<id>/...`.

O plugin:

1. autentica com um token JWT enviando `Authorization: Bearer <token>`;
2. faz o empréstimo (`POST /api/backend/rentals/checkout`);
3. lê o manifesto (`GET /api/backend/books/:id/manifest`);
4. baixa `readingOrder` (spine) + `resources` do epub-proxy, com barra de
   progresso;
5. sintetiza `META-INF/container.xml`, um `content.opf` (OPF 3.0) e um
   `nav.xhtml` (sumário) a partir dos metadados/toc do manifesto;
6. empacota tudo num `.epub` válido com `ffi/archiver` e abre para leitura.

## Instalação

Copie a pasta `meclivros.koplugin/` para o diretório de plugins do KOReader:

- **Kindle / Kobo / dispositivos:** `koreader/plugins/`
- **Desktop / emulador:** `~/.config/koreader/plugins/` (Linux) ou o diretório
  de dados equivalente da sua instalação.

Reinicie o KOReader. O menu **MEC Livros** aparecerá no menu principal
(ferramentas).

```
koreader/plugins/meclivros.koplugin/
├── _meta.lua
├── main.lua          # menu, diálogos e orquestração
├── api.lua           # cliente HTTP + endpoints
└── epubbuilder.lua   # reconstrução do EPUB a partir do manifesto
```

## Capturas de tela

<p align="center">
  <img src="screenshots/01_Menu.png" width="320" alt="Acesso ao MEC Livros pelo menu do KOReader"/><br/>
  <em>Acesse o MEC Livros pelo menu principal do KOReader.</em>
</p>

---

<p align="center">
  <img src="screenshots/02_menu.png" width="320" alt="Opções do plugin MEC Livros"/><br/>
  <em>O plugin reúne busca, empréstimos, conta e configuração de tokens.</em>
</p>

---

<p align="center">
  <img src="screenshots/03_buscar_livros.png" width="320" alt="Busca de livros por título ou autor"/><br/>
  <em>Busque livros por título ou autor.</em>
</p>

---

<p align="center">
  <img src="screenshots/04_emprestar_baixar.png" width="320" alt="Ações disponíveis para um livro"/><br/>
  <em>Escolha entre emprestar o livro completo ou baixar a amostra.</em>
</p>

---

<p align="center">
  <img src="screenshots/05_reading.png" width="320" alt="EPUB baixado aberto no KOReader"/><br/>
  <em>Leia no KOReader o EPUB reconstruído pelo plugin.</em>
</p>

---

<p align="center">
  <img src="screenshots/06_public-domain.png" width="320" alt="Busca de obras de domínio público"/><br/>
  <em>Obras de domínio público podem ser baixadas e lidas sem empréstimo.</em>
</p>

## Configuração dos tokens (recomendado: arquivo)

Não há login por usuário/senha: a autenticação do MEC Livros é federada pelo
**gov.br** (OAuth/OpenID Connect), com captcha e 2FA na tela do próprio gov.br.
Por isso o plugin usa os tokens já emitidos após o login no navegador.

A forma mais prática é por **arquivo de configuração**:

1. Copie [`meclivros_tokens.sample.lua`](meclivros_tokens.sample.lua) como
   `meclivros_tokens.lua`.
2. Preencha os dois valores, obtidos no navegador logado em
   <https://meclivros.mec.gov.br/> — DevTools (F12) → **Application → Cookies**:
   - `token` = cookie **`auth_token`**
   - `refresh_token` = cookie **`refresh_token`**
3. Copie o arquivo para a pasta de settings do KOReader:
   `koreader/settings/meclivros_tokens.lua`.
4. Abra o KOReader — o plugin importa automaticamente. (Ou force por
   **MEC Livros → Importar tokens do arquivo**.)

```lua
-- koreader/settings/meclivros_tokens.lua
return {
    token = "eyJhbGci...",          -- cookie auth_token
    refresh_token = "eyJhbGci...",  -- cookie refresh_token
}
```

O arquivo só precisa ser configurado **uma vez**. Com o `refresh_token`
(validade ~30 dias, renovada a cada uso), o plugin **renova o acesso sozinho**
quando o `auth_token` expira — sem recolar nada. Basta ler pelo menos uma vez
por mês para a sessão nunca expirar.

> Alternativa manual: **MEC Livros → Configurar token manualmente** permite
> colar só o JWT direto na interface, sem arquivo.

> ⚠️ O arquivo preenchido é um JWT com **dados pessoais** (nome, e-mail, CPF).
> Trate-o como segredo; ele fica salvo apenas no dispositivo e **não** deve ser
> versionado (o `.gitignore` já ignora `meclivros_tokens.lua`).

## Uso

1. **Minha conta** confirma que a autenticação funcionou.
2. **Buscar livros** → toque num resultado → **Emprestar e baixar (completo)**.
3. **Buscar domínio público** filtra o resultado pelo catálogo de obras públicas;
   toque num resultado → **Baixar e ler (domínio público)**, sem empréstimo.
4. **Meus empréstimos** lista os empréstimos ativos e permite **Baixar e ler**,
   **Renovar** ou **Devolver**.
5. **Pasta de download** define onde os EPUBs são gravados
   (padrão: `<home>/MEC Livros`).

## Amostra (demo) × livro completo

Sem empréstimo ativo, o manifesto da plataforma entrega apenas a **amostra**
(`is_demo: true`, ~10% via `demo_max_progress`) — só o livro **emprestado** vem
**completo**. Obras marcadas pela plataforma como de **domínio público** são a
exceção: podem ser baixadas diretamente. Por isso o menu do livro oferece:

- **Baixar amostra (demo)** — sempre disponível, sem empréstimo.
- **Emprestar e baixar (completo)** — faz o empréstimo e baixa o livro inteiro.
- **Baixar e ler (domínio público)** — disponível na busca de domínio público,
  sem empréstimo.

A plataforma permite **apenas 1 empréstimo ativo por vez**. Se você já tiver
outro livro emprestado, o plugin avisa e oferece **devolver o atual e emprestar
este** (você confirma antes).

## Limitações

- O livro **completo** exige empréstimo ativo daquele título (limite de 1 por
  vez), exceto obras de domínio público. Sem empréstimo, baixa-se apenas a
  amostra.
- Alguns livros são grandes (fontes e imagens embutidas); o download pode levar
  um tempo. A barra de progresso é interrompível.
- O plugin não implementa (ainda): paginação de resultados, favoritos,
  recomendações e sincronização de progresso de leitura com a plataforma.

## Licença

MIT. Veja [`LICENSE`](LICENSE).
