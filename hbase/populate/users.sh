adduser developer1 --gecos ",,," --disabled-password
echo "developer1:password" | chpasswd

adduser client1 --gecos ",,," --disabled-password
echo "client1:password" | chpasswd