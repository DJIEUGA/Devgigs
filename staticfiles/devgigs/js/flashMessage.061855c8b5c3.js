document.addEventListener('DOMContentLoaded', () => {

    // Close message component
    const closeMsgBtn = document.querySelectorAll('.closeMsg').forEach(btn => {
        btn.onclick = () => {
            document.querySelectorAll('.message').forEach(msg => {
                msg.style.display = 'none'
            })
        }
    })
})