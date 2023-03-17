import vyper
from vyper.interfaces import ERC20
from vyper.interfaces import ERC20Metadata
from vyper.interfaces import ERC721
from vyper.interfaces import ERC721Metadata
from vyper.interfaces import ERC721Enumerable
from vyper.interfaces import ERC1155
from vyper.interfaces import ERC1155Metadata
from vyper.interfaces import Contract

# Definir contrato de votación
contract Voting:
    # Estructura para almacenar información de votación
    votes: public(map(int128, int128))
    total_votes: public(int128)
    # Evento para registrar nuevos votos
    Vote: event({_from: address, candidate: int128})
    
    # Función para votar por un candidato
    def vote(self, candidate: int128):
        assert candidate >= 0
        assert candidate <= 9
        # Aumentar el contador de votos para el candidato
        self.votes[candidate] += 1
        # Incrementar el contador de votos totales
        self.total_votes += 1
        # Emitir un evento de voto
        log.Vote(msg.sender, candidate)
        
    # Función para obtener los resultados de la votación
    def get_results(self) -> dict:
        results = {}
        for i in range(10):
            results[i] = self.votes[i]
        return results
