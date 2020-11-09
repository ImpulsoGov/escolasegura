import streamlit as st

def genMonitorContainer():
    st.write(
        f"""
        <div class="container main-padding">
            <div>
                <p style="color:#2b14ff; font-size:21px;"><b>2.0 - O que fazer quando um caso for confirmado em uma unidade escolar?</b></p>
            </div>
            <div class="left-margin">
                    <div class="row">
                        <div class="col">
                            <div class="text-title-section minor-padding"> 
                            <img class="icon"
                            src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDQ4MCA0ODAiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgoJPHBvbHlnb24gc3R5bGU9IiIgcG9pbnRzPSIzNDQsNDAgMjcyLDQwIDI3Miw3MiAzMTIsNzIgMzEyLDQ0MCA1Niw0NDAgNTYsNzIgOTYsNzIgOTYsNDAgMjQsNDAgMjQsNDcyIDM0NCw0NzIgICIgZmlsbD0iIzVhNWE1YSIgZGF0YS1vcmlnaW5hbD0iI2JjYmNiYyIgY2xhc3M9IiI+PC9wb2x5Z29uPgoJPHBhdGggc3R5bGU9IiIgZD0iTTk2LDgwaDE3NnYtOFY0MGgtNTZjMC0xNy42NzItMTQuMzI4LTMyLTMyLTMycy0zMiwxNC4zMjgtMzIsMzJIOTZ2MzJWODB6IiBmaWxsPSIjNWE1YTVhIiBkYXRhLW9yaWdpbmFsPSIjYmNiY2JjIiBjbGFzcz0iIj48L3BhdGg+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik05Niw4MHYtOEg1NnYzNjhoMjU2VjcyaC00MHY4SDk2eiBNODgsMzc2aDE5Mkg4OHogTTI4MCwyMjRjMCw1My4wMTYtNDIuOTg0LDk2LTk2LDk2ICAgcy05Ni00Mi45ODQtOTYtOTZzNDIuOTg0LTk2LDk2LTk2UzI4MCwxNzAuOTg0LDI4MCwyMjR6IiBmaWxsPSIjZmZmZmZmIiBkYXRhLW9yaWdpbmFsPSIjZmZmZmZmIiBjbGFzcz0iIj48L3BhdGg+Cgk8cGF0aCBzdHlsZT0iIiBkPSJNMTg0LDEyOGMtNTMuMDE2LDAtOTYsNDIuOTg0LTk2LDk2czQyLjk4NCw5Niw5Niw5NnM5Ni00Mi45ODQsOTYtOTZTMjM3LjAxNiwxMjgsMTg0LDEyOHogTTI0OCwyNDggICBoLTQwdjQwaC00OHYtNDBoLTQwdi00OGg0MHYtNDBoNDh2NDBoNDBWMjQ4eiIgZmlsbD0iI2ZmZmZmZiIgZGF0YS1vcmlnaW5hbD0iI2ZmZmZmZiIgY2xhc3M9IiI+PC9wYXRoPgo8L2c+Cjxwb2x5Z29uIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgcG9pbnRzPSIyMDgsMTYwIDE2MCwxNjAgMTYwLDIwMCAxMjAsMjAwIDEyMCwyNDggMTYwLDI0OCAxNjAsMjg4IDIwOCwyODggMjA4LDI0OCAyNDgsMjQ4IDI0OCwyMDAgICAyMDgsMjAwICIgZmlsbD0iIzJiMTRmZiIgZGF0YS1vcmlnaW5hbD0iIzA2YjBjNyIgY2xhc3M9IiI+PC9wb2x5Z29uPgo8cG9seWdvbiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIHBvaW50cz0iNDU2LDI1NiA0NTYsODAgNDMyLDgwIDQwOCw4MCA0MDgsOTYgNDA4LDI1NiAiIGZpbGw9IiM1YTVhNWEiIGRhdGEtb3JpZ2luYWw9IiNiY2JjYmMiIGNsYXNzPSIiPjwvcG9seWdvbj4KPHJlY3QgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4PSI0MDgiIHk9IjI1NiIgc3R5bGU9IiIgd2lkdGg9IjQ4IiBoZWlnaHQ9IjMyIiBmaWxsPSIjMmIxNGZmIiBkYXRhLW9yaWdpbmFsPSIjMDZiMGM3IiBjbGFzcz0iIj48L3JlY3Q+Cjxwb2x5Z29uIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgcG9pbnRzPSI0MDgsNDA4IDQzMiw0NjQgNDU2LDQwOCA0NTYsMjg4IDQwOCwyODggIiBmaWxsPSIjNWE1YTVhIiBkYXRhLW9yaWdpbmFsPSIjYmNiY2JjIiBjbGFzcz0iIj48L3BvbHlnb24+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0iTTI0LDQ4MGgzMjBjNC40MTYsMCw4LTMuNTg0LDgtOFY0MGMwLTQuNDE2LTMuNTg0LTgtOC04aC03MmgtNDguODA4QzIxOS40OCwxMy43NjgsMjAzLjMyLDAsMTg0LDBzLTM1LjQ4LDEzLjc2OC0zOS4xOTIsMzIgIEg5NkgyNGMtNC40MTYsMC04LDMuNTg0LTgsOHY0MzJDMTYsNDc2LjQxNiwxOS41ODQsNDgwLDI0LDQ4MHogTTk2LDg4aDE3NmM0LjQxNiwwLDgtMy41ODQsOC04aDI0djM1Mkg2NFY4MGgyNCAgQzg4LDg0LjQxNiw5MS41ODQsODgsOTYsODh6IE0xNTIsNDhjNC40MTYsMCw4LTMuNTg0LDgtOGMwLTEzLjIzMiwxMC43NjgtMjQsMjQtMjRzMjQsMTAuNzY4LDI0LDI0YzAsNC40MTYsMy41ODQsOCw4LDhoNDh2MjRIMTA0ICBWNDhIMTUyeiBNMzIsNDhoNTZ2MTZINTZjLTQuNDE2LDAtOCwzLjU4NC04LDh2MzY4YzAsNC40MTYsMy41ODQsOCw4LDhoMjU2YzQuNDE2LDAsOC0zLjU4NCw4LThWNzJjMC00LjQxNi0zLjU4NC04LTgtOGgtMzJWNDhoNTYgIHY0MTZIMzJWNDh6IiBmaWxsPSIjMDAwMDAwIiBkYXRhLW9yaWdpbmFsPSIjMDAwMDAwIiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0iTTEyMCwyNTZoMzJ2MzJjMCw0LjQxNiwzLjU4NCw4LDgsOGg0OGM0LjQxNiwwLDgtMy41ODQsOC04di0zMmgzMmM0LjQxNiwwLDgtMy41ODQsOC04di00OGMwLTQuNDE2LTMuNTg0LTgtOC04aC0zMnYtMzIgIGMwLTQuNDE2LTMuNTg0LTgtOC04aC00OGMtNC40MTYsMC04LDMuNTg0LTgsOHYzMmgtMzJjLTQuNDE2LDAtOCwzLjU4NC04LDh2NDhDMTEyLDI1Mi40MTYsMTE1LjU4NCwyNTYsMTIwLDI1NnogTTEyOCwyMDhoMzIgIGM0LjQxNiwwLDgtMy41ODQsOC04di0zMmgzMnYzMmMwLDQuNDE2LDMuNTg0LDgsOCw4aDMydjMyaC0zMmMtNC40MTYsMC04LDMuNTg0LTgsOHYzMmgtMzJ2LTMyYzAtNC40MTYtMy41ODQtOC04LThoLTMyVjIwOHoiIGZpbGw9IiMwMDAwMDAiIGRhdGEtb3JpZ2luYWw9IiMwMDAwMDAiIHN0eWxlPSIiIGNsYXNzPSIiPjwvcGF0aD4KPHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBkPSJNMTg0LDMyOGM1Ny4zNDQsMCwxMDQtNDYuNjU2LDEwNC0xMDRzLTQ2LjY1Ni0xMDQtMTA0LTEwNFM4MCwxNjYuNjU2LDgwLDIyNFMxMjYuNjU2LDMyOCwxODQsMzI4eiBNMTg0LDEzNiAgYzQ4LjUyLDAsODgsMzkuNDgsODgsODhzLTM5LjQ4LDg4LTg4LDg4cy04OC0zOS40OC04OC04OFMxMzUuNDgsMTM2LDE4NCwxMzZ6IiBmaWxsPSIjMDAwMDAwIiBkYXRhLW9yaWdpbmFsPSIjMDAwMDAwIiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0iTTM5MiwxMDRoOHYxNTJ2MTUyYzAsMS4wOCwwLjIxNiwyLjE2LDAuNjQ4LDMuMTUyTDQyNCw0NjUuNjRWNDgwaDE2di0xNC4zNmwyMy4zNTItNTQuNDg4ICBDNDYzLjc4NCw0MTAuMTYsNDY0LDQwOS4wOCw0NjQsNDA4VjI1NlY4MGMwLTQuNDE2LTMuNTg0LTgtOC04aC0xNnYtOGgtMTZ2OGgtMTZjLTQuNDE2LDAtOCwzLjU4NC04LDh2OGgtMTZjLTQuNDE2LDAtOCwzLjU4NC04LDggIHYxNjhoMTZWMTA0eiBNNDQ4LDI4MGgtMzJ2LTE2aDMyVjI4MHogTTQzMiw0NDMuNjg4bC0xNi0zNy4zMzZWMjk2aDMydjExMC4zNkw0MzIsNDQzLjY4OHogTTQxNiw4OGgzMnYxNjBoLTMyVjg4eiIgZmlsbD0iIzAwMDAwMCIgZGF0YS1vcmlnaW5hbD0iIzAwMDAwMCIgc3R5bGU9IiIgY2xhc3M9IiI+PC9wYXRoPgo8cmVjdCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHg9Ijg4IiB5PSIzNjgiIHdpZHRoPSIxOTIiIGhlaWdodD0iMTYiIGZpbGw9IiMwMDAwMDAiIGRhdGEtb3JpZ2luYWw9IiMwMDAwMDAiIHN0eWxlPSIiIGNsYXNzPSIiPjwvcmVjdD4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPC9nPjwvc3ZnPg=="
                            title="Freepik" />
                            Plano de contingência</div>
                            <br>
                            <b><i>O que é?</b></i><br>É importante saber o que fazer no caso de algum caso confirmado de Covid-19 em escolas 
                            da sua rede. Veja uma ferramenta de reporte do caso para sua escola e monitoramento da rede.
                            <br><br><b><i>Quem usa?</i></b>
                            <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual.<br></li>
                            <br><b>➡️ Clique na imagem para acessar a ferramenta online ou <a href="https://docs.google.com/forms/d/1h5IxGK5S5dlMjiQKSI4e_6mxI_vk6DiXTJLV1C1Yh-0/copy">baixe aqui</a></b><br>
                        </div>
                        <div class="col"><br>
                            <div class="minor-padding">
                                <a href="https://docs.google.com/forms/d/1h5IxGK5S5dlMjiQKSI4e_6mxI_vk6DiXTJLV1C1Yh-0/copy" target="blank_">
                                    <img class="img-forms" src="https://i.imgur.com/oaFgwzQ.png">
                                </a>
                            </div>
                        </div>
                    </div>
                <div>
                    <p style="color:#2b14ff; font-size:21px;"><b>3.0 - Como acompanhar a notificação de casos em unidades escolares e orientar ações?</b></p>
                </div>
                <div class="row">
                    <div class="col">
                        <div class="text-title-section main-padding"> 
                            <img class="icon"
                            src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0ibTI5OC42Njc5NjkgNDI2LjY2Nzk2OWMwIDQ3LjEyODkwNi0zOC4yMDcwMzEgODUuMzMyMDMxLTg1LjMzNTkzOCA4NS4zMzIwMzEtNDcuMTI4OTA2IDAtODUuMzMyMDMxLTM4LjIwMzEyNS04NS4zMzIwMzEtODUuMzMyMDMxIDAtNDcuMTI4OTA3IDM4LjIwMzEyNS04NS4zMzU5MzggODUuMzMyMDMxLTg1LjMzNTkzOCA0Ny4xMjg5MDcgMCA4NS4zMzU5MzggMzguMjA3MDMxIDg1LjMzNTkzOCA4NS4zMzU5Mzh6bTAgMCIgZmlsbD0iIzJiMTRmMCIgZGF0YS1vcmlnaW5hbD0iI2ZmYTAwMCIgc3R5bGU9IiIgY2xhc3M9IiI+PC9wYXRoPjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0ibTM2Mi44MzU5MzggMjU0LjMxNjQwNmMtNzIuMzIwMzEzLTEwLjMyODEyNS0xMjguMTY3OTY5LTcyLjUxNTYyNS0xMjguMTY3OTY5LTE0Ny42NDg0MzcgMC0yMS4zMzU5MzggNC41NjI1LTQxLjU3ODEyNSAxMi42NDg0MzctNTkuOTQ5MjE5LTEwLjkyMTg3NS0yLjU1ODU5NC0yMi4yNjk1MzEtNC4wNTA3ODEtMzMuOTg0Mzc1LTQuMDUwNzgxLTgyLjM0Mzc1IDAtMTQ5LjMzMjAzMSA2Ni45ODQzNzUtMTQ5LjMzMjAzMSAxNDkuMzMyMDMxdjU5LjQ3NjU2MmMwIDQyLjIxODc1LTE4LjQ5NjA5NCA4Mi4wNzAzMTMtNTAuOTQ1MzEyIDEwOS41MDM5MDctOC4yOTY4NzYgNy4wODIwMzEtMTMuMDU0Njg4IDE3LjQyOTY4Ny0xMy4wNTQ2ODggMjguMzUxNTYyIDAgMjAuNTg5ODQ0IDE2Ljc0NjA5NCAzNy4zMzU5MzggMzcuMzMyMDMxIDM3LjMzNTkzOGgzNTJjMjAuNTg5ODQ0IDAgMzcuMzM1OTM4LTE2Ljc0NjA5NCAzNy4zMzU5MzgtMzcuMzM1OTM4IDAtMTAuOTIxODc1LTQuNzU3ODEzLTIxLjI2OTUzMS0xMy4yNjk1MzEtMjguNTQyOTY5LTMxLjQ4ODI4Mi0yNi42NDQ1MzEtNDkuNzUtNjUuMzI0MjE4LTUwLjU2MjUtMTA2LjQ3MjY1NnptMCAwIiBmaWxsPSIjMmIxNGZmIiBkYXRhLW9yaWdpbmFsPSIjZmZjMTA3IiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+PHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBkPSJtNDkwLjY2Nzk2OSAxMDYuNjY3OTY5YzAgNTguOTEwMTU2LTQ3Ljc1NzgxMyAxMDYuNjY0MDYyLTEwNi42Njc5NjkgMTA2LjY2NDA2MnMtMTA2LjY2Nzk2OS00Ny43NTM5MDYtMTA2LjY2Nzk2OS0xMDYuNjY0MDYyYzAtNTguOTEwMTU3IDQ3Ljc1NzgxMy0xMDYuNjY3OTY5IDEwNi42Njc5NjktMTA2LjY2Nzk2OXMxMDYuNjY3OTY5IDQ3Ljc1NzgxMiAxMDYuNjY3OTY5IDEwNi42Njc5Njl6bTAgMCIgZmlsbD0iI2ZmOTE0NyIgZGF0YS1vcmlnaW5hbD0iI2Y0NDMzNiIgc3R5bGU9IiIgY2xhc3M9IiI+PC9wYXRoPjwvZz48L3N2Zz4="
                            title= "Freepik" />
                            Ferramenta de notificação
                        </div>
                        <br>
                        <b><i>O que é?</b></i><br>
                        Ferramenta de comunicação das escolas com as Secretarias de Educação e Saúde sobre a existência de um caso ou suspeita na unidade.
                        <br><br><b><i>Como usa?</b></i>
                        <ol>
                            <li>Gestor(a) da Secretaria de Educação Municipal ou Estadual envia o formulário para as escolas de sua rede;</li>
                            <li>No surgimento de um caso ou suspeita, diretores(as) utilizam o formulário para informar para a Secretaria de Educação e Saúde, e seguem o plano de ação indicado.</li>
                        </ol>
                        <br><b>➡️ Clique na imagem para acessar a ferramenta online ou </b><a href="https://docs.google.com/forms/d/1xh-_NI925-bWNn81PG5dKKkSa9J14NVwT3SpPIShJzo/copy">baixe aqui</a></b><br>
                    </div>
                    <div class="col"><br>
                        <div class="main-padding">
                            <a href="https://docs.google.com/forms/d/1xh-_NI925-bWNn81PG5dKKkSa9J14NVwT3SpPIShJzo/copy" target="_blank">
                            <img class="img-forms" src="https://i.imgur.com/nhx3ZGB.png"> 
                        </div>
                        </a>
                    </div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    
if __name__ == "__main__":
    main()
