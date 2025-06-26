document.addEventListener('DOMContentLoaded', function() {
    const botaoMenuMobile = document.getElementById('botaoMenuMobile');
    const navegacao = document.querySelector('.navegacao');
    
    if(botaoMenuMobile && navegacao) {
        botaoMenuMobile.addEventListener('click', function() {
            navegacao.classList.toggle('ativo');
            this.querySelector('i').classList.toggle('fa-bars');
            this.querySelector('i').classList.toggle('fa-times');
        });
    }

    const botoesAba = document.querySelectorAll('.botao-aba');
    const conteudosAba = document.querySelectorAll('.conteudo-aba');
    
    botoesAba.forEach(botao => {
        botao.addEventListener('click', function() {
            const idAba = this.getAttribute('data-aba');
            botoesAba.forEach(b => b.classList.remove('ativo'));
            conteudosAba.forEach(conteudo => conteudo.classList.remove('ativo'));
            this.classList.add('ativo');
            const conteudoAlvo = document.getElementById(idAba);
            if(conteudoAlvo) conteudoAlvo.classList.add('ativo');
        });
    });

    function gerarToken() {
        const exibicaoToken = document.getElementById('exibicaoToken');
        if (!exibicaoToken) return;
        const codigoToken = exibicaoToken.querySelector('.codigo-token');
        
        setInterval(() => {
            const novoToken = Math.floor(100000 + Math.random() * 900000);
            codigoToken.textContent = novoToken;
        }, 30000);
    }
    
    gerarToken();

    const botaoVerificarSeguranca = document.getElementById('botaoVerificarSeguranca');
    const secaoVerificacao = document.getElementById('verificacaoSeguranca');
    const barraMedidor = document.getElementById('barraMedidor');
    
    if (botaoVerificarSeguranca && secaoVerificacao && barraMedidor) {
        botaoVerificarSeguranca.addEventListener('click', function(e) {
            e.preventDefault();
            secaoVerificacao.scrollIntoView({ behavior: 'smooth' });
            setTimeout(() => {
                barraMedidor.style.width = '70%';
            }, 500);
        });
    }

    const botaoMelhorarSeguranca = document.getElementById('botaoMelhorarSeguranca');
    
    if (botaoMelhorarSeguranca && barraMedidor) {
        botaoMelhorarSeguranca.addEventListener('click', function() {
            alert('Um especialista em segurança entrará em contato para ajudar a melhorar suas configurações de segurança.');
            barraMedidor.style.width = '100%';
            barraMedidor.style.backgroundColor = '#00ff00';
        });
    }

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const idAlvo = this.getAttribute('href');
            if (idAlvo === '#') return;
            const elementoAlvo = document.querySelector(idAlvo);
            if (elementoAlvo) {
                elementoAlvo.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    function animarAoRolar() {
        const elementos = document.querySelectorAll('.cartao-servico, .conteudo-recurso, .etapa');
        elementos.forEach(elemento => {
            const posicaoElemento = elemento.getBoundingClientRect().top;
            const posicaoTela = window.innerHeight / 1.3;
            if (posicaoElemento < posicaoTela) {
                elemento.style.opacity = '1';
                elemento.style.transform = 'translateY(0)';
            }
        });
    }
    
    const elementosAnimados = document.querySelectorAll('.cartao-servico, .conteudo-recurso, .etapa');
    elementosAnimados.forEach(elemento => {
        elemento.style.opacity = '0';
        elemento.style.transform = 'translateY(20px)';
        elemento.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    });
    
    window.addEventListener('scroll', animarAoRolar);
    animarAoRolar();
});
