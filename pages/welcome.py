import streamlit as st
from time import sleep

def about_blog():
    """Função que apresenta informações sobre o Blog"""

    st.title("✨ Bem-Vindo ao Blog! ✨")

    st.caption("É muito bom te ver aqui! 🌟 Nessa plataforma, você poderá ler e criar diversos posts sobre qualquer assunto. "
        "Aqui, criatividade e imaginação andam de mãos dadas, unindo-se às maiores forças do ser humano. "
        "Sinta-se livre para compartilhar seus aprendizados e ideias com o mundo! 🌍")

    st.divider()

    # Motivo da Criação do Blog
    st.subheader("💡 Por que este Blog foi criado?")
    st.caption("Criar este blog usando `Python` e `Streamlit` é uma experiência divertida e desafiadora! "
        "É uma oportunidade de colocar meus conhecimentos em prática, compartilhar aprendizado e me preparar para projetos profissionais. 🚀")

    st.divider()

    # Assuntos do Blog
    st.subheader("📚 Quais assuntos constituem estes Blogs?")
    st.caption("Neste blog, qualquer tema é bem-vindo! 🌈 A única limitação é sua imaginação. "
        "Prepare-se para explorar conteúdos variados e, quem sabe, criar os seus próprios! ✏️")

    st.divider()

    # Explicação do Blog
    st.subheader("📖 Como começar a leitura?")
    st.caption("Use a barra lateral à esquerda para navegar. Existem seções e páginas separadas por propósito. "
        "Explore cada área e descubra conteúdos que você vai adorar! 🔍")

    st.divider()

    with st.popover("🚀 Áreas que você pode explorar", use_container_width=True):
        st.caption("Algumas áreas interessantes para começar sua jornada:")

        # Criar colunas para os botões
        col1, col2 = st.columns(2)

        with col1:
            create_blog_button = st.button(":material/add: Criar um Blog", type="primary")
            if create_blog_button:
                st.success("Preparando a página de criação...")
                sleep(1)
                st.switch_page("pages/create.py")

        with col2:
            about_project_button = st.button(":material/info: Ver sobre este projeto", type="primary")
            if about_project_button:
                st.info("Mergulhando na curiosidade...")
                sleep(1)
                st.switch_page("pages/about.py")


def main():
    about_blog()


main()
