#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/tcp.h>
#include <arpa/inet.h>
//#include sock.h


// -> Variáveis:

int PortNumber = 16340;
int BuffSize = 255;
int MaxConnects = 8;

void report(const char* tocar, int num) {
  perror(tocar);
  if (num) exit(-1); 
}

int main() {                   // chamada do socket
  int fd = socket(AF_INET,     
                  SOCK_STREAM, /* tamanho de carga útil fiável, bidireccional e arbitrária */
                  0);          /* protocol (TCP) */
  if (fd < 0) report("socket", 1); /* terminar */

  /* Ligar em memória o endereço local do servidor */
  struct sockaddr_in saddr;
  memset(&saddr, 0, sizeof(saddr));          /* limpar os bytes */
  saddr.sin_family = AF_INET;                
  saddr.sin_addr.s_addr = htonl(INADDR_ANY); /* host-to-network endian */
  saddr.sin_port = htons(PortNumber);        /* listening */

  if (bind(fd, (struct sockaddr *) &saddr, sizeof(saddr)) < 0)
    report("bind", 1); /* terminar */

  /* soquete ouve*/
  if (listen(fd, MaxConnects) < 0) /* lista de clientes, solicitações*/
    report("listen", 1); /* terminar */

  fprintf(stderr, "Listening on port %i for clients...\n", PortNumber);

  /* Um servidor ouve tradicionalmente indefinidamente*/

  //while (1) {
  int i;
  for (i = 0; i < 2; i++){

    struct sockaddr_in caddr; /* endereço do cliente */
    int len = sizeof(caddr);  /* o comprimento do endereço pode mudar*/

    // sockaddr* é uma estrutura que contém o endereço de internet
    int client_fd = accept(fd, (struct sockaddr*) &caddr, &len);  /* aceitar uma solicitação do cliente.  */
    if (client_fd < 0) {
      report("accept", 0); /* não interromper, mesmo tendo problemas */
      continue;
    }

    /* lendo o cliente */
    //for (i = 0; i < 2; i++) {
      char buffer[BuffSize + 1];
      memset(buffer, '\0', sizeof(buffer));
      int count = read(client_fd, buffer, sizeof(buffer));
      if (count > 0) {
        puts(buffer);
        write(client_fd, buffer, sizeof(buffer)); /* confirmação de leitura*/
    }
    //}
    close(client_fd); /* parar conexão */
  }  /* while(1) */
  return 0;
}

// para se comunicar -> echo [msg] | netcat localhost 16340
