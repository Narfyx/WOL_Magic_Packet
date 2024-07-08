import socket


def send_magic_packet(mac_address):
    # Nettoyage de l'adresse MAC pour enlever les séparateurs
    mac_address = mac_address.replace(":", "").replace("-", "").replace(".", "")

    if len(mac_address) != 12:
        raise ValueError("Adresse MAC invalide")

    # Construction du Magic Packet
    magic_packet = bytes.fromhex("FF" * 6 + mac_address * 16)

    # Création d'un socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Activation de l'option broadcast
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Envoi du paquet sur le réseau local à l'adresse de broadcast
        sock.sendto(magic_packet, ("<broadcast>", 9))


# Exemple d'utilisation avec une adresse MAC
mac = "00:11:22:33:44:55"
send_magic_packet(mac)
