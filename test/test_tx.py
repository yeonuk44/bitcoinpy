import tx
from io import BytesIO

# test legacy tx
legacy_tx_hex = "0100000001813f79011acb80925dfe69b3def355fe914bd1d96a3f5f71bf8303c6a989c7d1000000006b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278afeffffff02a135ef01000000001976a914bc3b654dca7e56b04dca18f2566cdaf02e8d9ada88ac99c39800000000001976a9141c4bc762dd5423e332166702cb75f40df79fea1288ac19430600"
stream = BytesIO(bytes.fromhex(legacy_tx_hex))
tx_obj = tx.parse(stream)
print(tx_obj)
tx.verify(tx_obj, testnet=False)

tx_bytes = tx.serialize(tx_obj)
print(tx_bytes)
if tx_bytes == bytes.fromhex(legacy_tx_hex):
    print("legacy: serialized!")

# test segwit tx
# p2sh-p2wpkh
segwit_tx_hex = "02000000000101fb745ed7da899f898954ae4b9d53e2f5733dc66ee9f53f437febc3dd1001f15e00000000171600145bbcf04653f3f782a060168801fd0687b3672ce2feffffff02100b3a8b0100000017a914eb4b7c2b71ae0f6850cc2a58a92d53c9ab294d8c8779b61a00000000001976a914e4c8b088f49dbc6a2248400e5002d2a29aed695388ac0247304402204f3934b856ee128dc25d2c5b825dd7d035911162bd8bf9f0a3dec1496c3cd32c0220324a0a2f9572573786ac5013e0db7fdeb92ee853ae1429901fe7cfd6242a98f2012102bace1110a291ccaad9a3fdd14ce705a92336024e4f9e29b9e6014fa3afd3c7776a671900"
stream = BytesIO(bytes.fromhex(segwit_tx_hex))
tx_obj = tx.parse(stream)
print(tx_obj)
tx.verify(tx_obj, testnet=True)

tx_bytes = tx.serialize(tx_obj)
print(tx_bytes)
if tx_bytes == bytes.fromhex(segwit_tx_hex):
    print("segwit: serialized!")
