import streamlit as st
import unicodedata


def set_config():
    """Função responsável por definir as configurações
    gerais das páginas."""

    st.set_page_config (
        page_title = "Blog",
        page_icon = "🗒️",
        layout = "centered"
    )


def is_emoji(text: str) -> bool:
    """
    Função responsável por avaliar um emoji e retornar
    se este é válido ou não.
    """

    if len(text) != 1:
        return False

    category = unicodedata.category(text)

    return category == "So"


def set_style():
    """Função responsável por definir o estilo das páginas."""

    st.markdown("""<style>
    header.st-emotion-cache-1pru02b.e16b601d7 {
        color: white;
        font-size: 1em;
        font-weight: bolder;
        border: 0px;
        margin: 0px;
    }

    h3#voce-pode-explorar-estas-areas {
        color: #a3a3a3;
    }

    h1#titulo, h1#conteudo, h1#icone {
        margin: 0px;
        padding: 0px;
    }
</style>""", unsafe_allow_html = True)


def main():
    set_config()
    set_style()


main()
