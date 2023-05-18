# Importo matplotlib
import matplotlib.pyplot as plt
#Pandas
import pandas as pd
# Importo API de Llama Protocol
from llama import DefiLlama
# Instancio API de Llama Protocol
defillama = DefiLlama()

# Obtengo datos de TVL
tvl = defillama.get_tvl()

# Obtengo datos de TVL por protocolo
tvl_protocol = defillama.get_tvl_protocol()

# Obtengo datos de TVL por protocolo y cadena
tvl_protocol_chain = defillama.get_tvl_protocol_chain()

# Diccionario con los datos de TVL por protocolo y cadena
tvl_protocol_chain_dict = {}
for protocol in tvl_protocol_chain:
    for chain in tvl_protocol_chain[protocol]:
        if protocol not in tvl_protocol_chain_dict:
            tvl_protocol_chain_dict[protocol] = {}
        tvl_protocol_chain_dict[protocol][chain] = tvl_protocol_chain[protocol][chain]

# Armo gráfico de barras con los datos de TVL por protocolo y cadena
# Armo una lista con los datos de TVL por protocolo y cadena
tvl_protocol_chain_list = []
for protocol in tvl_protocol_chain_dict:
    for chain in tvl_protocol_chain_dict[protocol]:
        tvl_protocol_chain_list.append([protocol, chain, tvl_protocol_chain_dict[protocol][chain]])

# Ordeno la lista de mayor a menor
tvl_protocol_chain_list.sort(key=lambda x: x[2], reverse=True)

# Obtengo los 10 primeros
tvl_protocol_chain_list = tvl_protocol_chain_list[:10]

# Obtengo los datos de TVL por protocolo y cadena en listas separadas
protocols = [x[0] for x in tvl_protocol_chain_list]
chains = [x[1] for x in tvl_protocol_chain_list]
tvls = [x[2] for x in tvl_protocol_chain_list]

# Grafico
plt.bar(range(len(tvls)), tvls, align='center')
plt.xticks(range(len(tvls)), chains)
plt.xlabel('Chain')

# Muestro el gráfico
plt.show()


