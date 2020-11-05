import streamlit as st

def genPrepareContainer():
    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section"><img class="square" src="https://i.imgur.com/gGIFS5N.png">Prepare 
            <p>Prepare os protocolos de segurança, de acompanhamento e canais de comunicação para a reabertura das escolas.</p>
            </div>
            <p><b>A fase de preparação é onde os protocolos de segurança das escolas são discutidas e pactuadas.</b> 
            Durante a reabertura, é importante que seja estabelecida uma rotina de verificação das unidades escolares 
            para acompanhar o cumprimento dos protocolos estabelecidos.</p>
                <div class="left-margin">
                    <div class="text-title-section minor-padding"> 
                    <img class="icon"
                    src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0zNTQuNjY5LDE2NC4wNTVjLTY1LjMyNiwwLTUwLjIyOC0yOS43NDMtOTguNjY5LTI5Ljc0M3MtMzMuMzQzLDI5Ljc0My05OC42NjksMjkuNzQzICBsMzAuNjQ5LDExMi4wNDloMTM2LjAzOEwzNTQuNjY5LDE2NC4wNTV6IiBmaWxsPSIjM2M0NzRkIiBkYXRhLW9yaWdpbmFsPSIjM2M0NzRkIiBjbGFzcz0iIj48L3BhdGg+CjxjaXJjbGUgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBjeD0iMTExLjY4MiIgY3k9IjI2Ni4wMDciIHI9IjExMS42ODIiIGZpbGw9IiM1YTVhNWEiIGRhdGEtb3JpZ2luYWw9IiM0NjUwNTkiIGNsYXNzPSIiPjwvY2lyY2xlPgo8Y2lyY2xlIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgY3g9IjExMS42ODIiIGN5PSIyNjYuMDA3IiByPSI3Ni4yOTUiIGZpbGw9IiM5OWZmZDQiIGRhdGEtb3JpZ2luYWw9IiMzYWM3YjQiIGNsYXNzPSIiPjwvY2lyY2xlPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0xMzIuMjg5LDMyMS43MDRjLTQyLjEzNywwLTc2LjI5Ni0zNC4xNTktNzYuMjk2LTc2LjI5NmMwLTE1LjgwMiw0LjgwNS0zMC40ODMsMTMuMDMyLTQyLjY2MSAgYy0yMC4yOTQsMTMuNzEyLTMzLjYzNSwzNi45My0zMy42MzUsNjMuMjY0YzAsNDIuMTM3LDM0LjE1OSw3Ni4yOTYsNzYuMjk2LDc2LjI5NmMyNi4zMzUsMCw0OS41NTMtMTMuMzQyLDYzLjI2NC0zMy42MzUgIEMxNjIuNzcyLDMxNi45LDE0OC4wOTEsMzIxLjcwNCwxMzIuMjg5LDMyMS43MDR6IiBmaWxsPSIjMDBhZDk0IiBkYXRhLW9yaWdpbmFsPSIjMDBhZDk0IiBjbGFzcz0iIj48L3BhdGg+CjxjaXJjbGUgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBjeD0iNDAwLjMxOCIgY3k9IjI2Ni4wMDciIHI9IjExMS42ODIiIGZpbGw9IiM1YTVhNWEiIGRhdGEtb3JpZ2luYWw9IiM0NjUwNTkiIGNsYXNzPSIiPjwvY2lyY2xlPgo8Y2lyY2xlIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgY3g9IjQwMC4zMTgiIGN5PSIyNjYuMDA3IiByPSI3Ni4yOTUiIGZpbGw9IiM5OWZmZDQiIGRhdGEtb3JpZ2luYWw9IiMzYWM3YjQiIGNsYXNzPSIiPjwvY2lyY2xlPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik00MjAuOTE5LDMyMS43MDRjLTQyLjEzNywwLTc2LjI5Ni0zNC4xNTktNzYuMjk2LTc2LjI5NmMwLTE1LjgwMiw0LjgwNS0zMC40ODMsMTMuMDMyLTQyLjY2MSAgYy0yMC4yOTQsMTMuNzEyLTMzLjYzNSwzNi45My0zMy42MzUsNjMuMjY0YzAsNDIuMTM3LDM0LjE1OSw3Ni4yOTYsNzYuMjk2LDc2LjI5NmMyNi4zMzUsMCw0OS41NTMtMTMuMzQyLDYzLjI2NC0zMy42MzUgIEM0NTEuNDAyLDMxNi45LDQzNi43MjIsMzIxLjcwNCw0MjAuOTE5LDMyMS43MDR6IiBmaWxsPSIjMDBhZDk0IiBkYXRhLW9yaWdpbmFsPSIjMDBhZDk0IiBjbGFzcz0iIj48L3BhdGg+CjxjaXJjbGUgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBjeD0iMjU2IiBjeT0iMTg2LjE5OSIgcj0iMTYuMzE1IiBmaWxsPSIjZmY5MTQ3IiBkYXRhLW9yaWdpbmFsPSIjZGE1YjY1IiBjbGFzcz0iIj48L2NpcmNsZT4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPC9nPjwvc3ZnPg=="
                    title="Freepik" />
                     Ferramenta de verificação</div>
                    <br>
                    <div class="row">
                        <div class="col">
                            <div>
                            <b><i>O que é?</b></i><br>
                            Formulário para conferir a adequação das unidades escolares aos protocolos estabelecidos e indicar orientações.
                            <br><br>
                            <b><i>Quem usa?</b></i>
                            <li>Gestor(a) da Secretaria de Educação Municipal ou Estadual: obtém o formulário e envia para diretores(as).</li>
                            <li>Diretores(as) escolares: preenchem o formulário para verificação da Secretaria.</li>
                            <br><br><b>➡️ Clique na imagem para acessar a ferramenta online</b>
                            </div>
                        </div>
                        <div class="col">
                            <a href="https://docs.google.com/forms/d/1JjXIs0M-A-RLhISYlltX4fjXL5pu8C_iKUkI_a8GhyI/copy" target="_blank">
                            <img class="img-forms" src="https://i.imgur.com/oZoaayW.png"> 
                            </a>
                        </div>
                    </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()