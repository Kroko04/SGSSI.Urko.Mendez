#!/bin/bash

# 1. Pedir IP
read -p "Introduce IP a bloquear: " IP_OBJETIVO

# 2. Salir si está vacío
[ -z "$IP_OBJETIVO" ] && exit 1

# 3. Bloquear
sudo iptables -A INPUT -s $IP_OBJETIVO -j DROP

# 4. Confirmar y Listar la regla específica
if [ $? -eq 0 ]; then
    echo ">> IP Bloqueada con éxito. Verificando lista:"
    sudo iptables -L INPUT -n -v | grep "$IP_OBJETIVO"
fi
