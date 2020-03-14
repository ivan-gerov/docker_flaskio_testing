let socket = io.connect('http://' + document.domain + ':' + location.port)

function send_connect() {
    socket.emit('connected')
}

socket.on('greeting', greeting => {
    console.log(greeting)
})