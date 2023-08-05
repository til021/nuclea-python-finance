import yfinance as yf
from datetime import date


def obter_dados_acao():
    while True:
        ticker = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
        nome_arquivo = ticker + "_" + str(date.today()) + ".txt"

        try:
            # Obter os dados da ação usando o Yahoo Finance (B3)
            acao = yf.download(ticker + ".SA", progress=False)

            # Exibir os dados

            with open(nome_arquivo, "w") as arquivo:
                arquivo.write("Relatorio da acao: " + ticker + "\n")
                arquivo.write(str(acao.tail()))

            print(f"Relatório exportado com sucesso para o arquivo '{nome_arquivo}'.")
            return

        except Exception as e:
            print(
                "Erro ao obter dados da ação. Verifique o código da ação e tente novamente."
            )
            print(f"Detalhes do erro: {e}")


if __name__ == "__main__":
    obter_dados_acao()
