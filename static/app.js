$(document).ready(function(){

    //Conecta con el websocket server (en caso de usar namespace, añadirlo a la uri)
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    
    // Escucha al evento 'saludo' emitido por el servidor
    socket.on('saludo', function(data) {
        console.log("Respuesta: "+data.msg);
    });
});