import streamlit as st


def content():
    """
    Função responsável por apresentar sobre mim (criador) e sobre a
    plataforma (blog)
    """

    st.title(":material/info: Sobre")
    st.caption("Olá, seja bem-vindo! Nesta página, você verá sobre o que se trata esta plataforma.")

    st.subheader("Minha jornada até aqui")
    st.caption("👋🏻 Prazer a você, meu nome é **Flame**, sou o criador e responsável por essa plataforma. Desde pequeno, eu sempre quis **programar**. Ver os códigos era coisa de outro mundo. Para mim, **apenas Einstein ou Nikola Tesla seria capaz de programar**. A realidade que ninguém conta é que até **crianças podem (e devem) começar a programar***. Programar **estimula** várias partes do cérebro e **cria habilidades fantásticas**, como o **raciocínio lógico**, **a disciplina**, **a criatividade** e a **imaginação**, aprendizado de coisas novas e até quem saiba o **desenvolvimento profissional**, entre outros...")

    st.caption("🗯️ Sabendo desses benefícios, eu decidi tentar **começar** a programar. ⏳ Em mais ou menos maio de 2024 eu comecei com HTML e CSS. Isso não durou muito tempo, programei alguns sites beeeem básicos, mas depois eu sai por um tempo... Já em outubro de 2024 eu voltei novamente, agora sim com uma vontade insana de criar sites. Fiz mais de 10 cursos, e encarei a programação como algo mais sério. 👍🏻 Após mais ou menos 1 mês, eu estava criando sites legais apenas com HTML e CSS. Eu já tinha me aprofundado em alguns termos como **Front-End**, **Back-End** e **Full-Stack**. De ínico, sempre pensei em ser Front-End (programador responsável por criar a interface do usuário - como a página de um site, seus elementos e estilos), mas após mais um tempo, percebi que essa área eu **não gostava** mais. ☹️ Criar páginas com HTML e CSS de repente ficou chato. Até que um tempo depois, eu decidi **aprender o básico de JavaScript**, pois eu saberia que agora sim seria um **desafio real** aprender uma linguagem de programação. Aprendi o raso do JavaScript, mas mesmo assim **não gostei de Front-End**. 💫 Parei de aprender JavaScript após alguns dias, e eu vi algo chamado **Python**, que foi o que **mudou minha trajetória**. A partir disso, nos primeiros dias eu achei a linguagem muito fácil, muito leve de se trabalhar. Pesquisei bastante sobre essa linguagem, fiz diversos cursos e me apaixonei, assim tornando essa a minha **linguagem principal**. Python oferece bibliotecas de IA, análise de dados, criação de **páginas web** (Streamlit foi usado para criar essa plataforma), e entre outras funcionalidades que python possui. 🧠 Desde então fui devorando o conhecimento todo dessa linguagem, e hoje busco aprimorar mais ainda e conhecer mais bibliotecas e mais funcionalidades dessa linguagem. Essa jornada apenas está começando, e isso me mostra que **programar não é dificil!** apenas exige dedicação e disciplina. 💪🏻")

    st.subheader("Sobre a plataforma")
    st.caption("Fazer essa plataforma é bem desafiador, mas também muito recompensador para mim. Ao fazer plataformas como essa, posso obter diversos benefícios. Esta plataforma representa um projeto grande, o que significa que é um preparatório, como por exemplo útil para profissionalismo. Meu objetivo criando estes projetos é **👷🏻‍♂️ organizar código e blocos de código, como um arquiteto**, **🐍 aprimoramento da linguagem Python**, **🔼 crescimento do pensamento lógico**, **💫 simular projetos reais**, entre outros. Programar é uma atividade muito essencial nos dias de hoje, onde a tecnologia está no pico de crescimento, e cada vez mais crescendo. Em outras palavras, fazer essa plataforma significa muito para mim, é um lugar aonde coloco em prática minhas habilidades e até aprendo mais. 🛥️ Continuarei a fazer projetos Streamlit até eu me aprimorar bastante nessa jornada!")


    st.subheader("Sobre mim")
    with st.expander("Saiba mais sobre mim"):
        github_link = "https://github.com/Flame77OFC"
        github_button = st.link_button("Meu perfil do GitHub", type="primary", url=github_link)


def main():
    content()


main()
