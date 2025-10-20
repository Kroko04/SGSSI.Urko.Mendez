// Validación DNI
function validarDNI(dni) {
    const regex = /^(\d{8})[- ]?([A-Z])$/;
    const letras = 'TRWAGMYFPDXBNJZSQVHLCKE';
    
    if (!regex.test(dni)) return false;
    
    const [_, numero, letra] = regex.exec(dni);
    const letraCalculada = letras[numero % 23];
    
    return letra === letraCalculada;
}

// Validación formulario registro
document.getElementById('register_form')?.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    const dni = formData.get('dni');
    const telefono = formData.get('telefono');
    const nombre = formData.get('nombre');
    const apellidos = formData.get('apellidos');
    const email = formData.get('email');
    
    // Validaciones
    if (!/^[A-Za-zÁáÉéÍíÓóÚúÑñ\s]+$/.test(nombre)) {
        alert('El nombre solo puede contener texto');
        return;
    }
    
    if (!/^[A-Za-zÁáÉéÍíÓóÚúÑñ\s]+$/.test(apellidos)) {
        alert('Los apellidos solo pueden contener texto');
        return;
    }
    
    if (!validarDNI(dni)) {
        alert('DNI no válido');
        return;
    }
    
    if (!/^\d{9}$/.test(telefono)) {
        alert('Teléfono debe tener 9 dígitos');
        return;
    }
    
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        alert('Email no válido');
        return;
    }
    
    // Si pasa todas las validaciones, enviar formulario
    this.submit();
});

// Validación formulario login
document.getElementById('login_form')?.addEventListener('submit', function(e) {
    e.preventDefault();
    // Validaciones básicas
    this.submit();
});