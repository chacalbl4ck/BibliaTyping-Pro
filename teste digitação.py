import random
import time
import tkinter as tk
from tkinter import messagebox

# ============================================================
#  TEXT_POOL — 50 TRECHOS COMPLETOS DA BÍBLIA
# ============================================================

TEXT_POOL = [

    # 1
    """No princípio, criou Deus os céus e a terra. A terra estava sem forma e vazia, trevas cobriam o abismo, mas o Espírito de Deus pairava sobre as águas. Então disse Deus: Haja luz; e a luz passou a existir. Deus viu que a luz era boa e separou a luz das trevas, chamando à luz Dia e às trevas Noite. Assim se completou o primeiro dia, marcando o início da ordem divina sobre a criação.""",

    # 2
    """O Senhor é o meu pastor; nada me faltará. Ele me faz repousar em pastos verdejantes e guia-me às águas de descanso. Restaura a minha alma e conduz-me pelas veredas da justiça por amor do seu nome. Ainda que eu ande pelo vale da sombra da morte, não temerei mal algum, porque tu estás comigo; teu bordão e teu cajado me consolam e me sustentam.""",

    # 3
    """Bem-aventurados os pobres de espírito, porque deles é o reino dos céus. Bem-aventurados os que choram, porque serão consolados. Bem-aventurados os mansos, pois herdarão a terra. Bem-aventurados os que têm fome e sede de justiça, porque serão fartos. Bem-aventurados os misericordiosos, porque alcançarão misericórdia, e bem-aventurados os limpos de coração, pois verão a Deus.""",

    # 4
    """Porque Deus amou ao mundo de tal maneira que deu o seu Filho unigênito, para que todo o que nele crer não pereça, mas tenha a vida eterna. Deus enviou o Filho ao mundo não para condená-lo, mas para que por meio dele o mundo fosse salvo. Quem crê não é julgado; quem não crê já está condenado por rejeitar a luz que veio ao mundo.""",

    # 5
    """No princípio era o Verbo, e o Verbo estava com Deus, e o Verbo era Deus. Ele estava no princípio com Deus e todas as coisas foram feitas por meio dele. Sem Ele nada do que existe teria sido feito. Nele estava a vida, e a vida era a luz dos homens. A luz resplandece nas trevas, e as trevas não prevaleceram contra ela.""",

    # 6
    """Confia no Senhor de todo o teu coração e não te apoies no teu próprio entendimento. Reconhece-o em todos os teus caminhos, e Ele endireitará as tuas veredas. Não sejas sábio aos teus próprios olhos; teme ao Senhor e aparta-te do mal. Isto trará saúde ao teu corpo e refrigério aos teus ossos.""",

    # 7
    """Aquele que habita no esconderijo do Altíssimo e descansa à sombra do Onipotente pode declarar: Tu és o meu refúgio e a minha fortaleza, o meu Deus em quem confio. Ele te livrará do laço do inimigo e da peste destruidora. Com suas asas te cobrirá e estarás seguro; sua fidelidade será escudo e proteção.""",

    # 8
    """Tudo tem o seu tempo determinado, e há tempo para todo propósito debaixo do céu: tempo de nascer e tempo de morrer; tempo de plantar e tempo de colher o que se plantou; tempo de matar e tempo de curar; tempo de derrubar e tempo de construir; tempo de chorar e tempo de rir; tempo de prantear e tempo de dançar.""",

    # 9
    """O amor é paciente, é bondoso. O amor não arde em ciúmes, não se vangloria, não se orgulha, não se porta de maneira inconveniente. Não busca seus próprios interesses, não se irrita facilmente, não guarda rancor. O amor tudo sofre, tudo crê, tudo espera, tudo suporta. O amor jamais acaba, permanecendo para sempre.""",

    # 10
    """Ensina-nos a contar os nossos dias, para que alcancemos coração sábio. Volta-te para nós, Senhor; até quando? Tem compaixão dos teus servos. Sacia-nos de manhã com a tua bondade, para que nos alegremos por todos os nossos dias. Confirma sobre nós a obra das nossas mãos, e firma os nossos passos no teu caminho.""",

    # 11
    """O Senhor é bom e uma fortaleza no dia da angústia; Ele conhece aqueles que se refugiam Nele. Ainda que o adversário avance como enchente impetuosa, o Senhor permanece firme como rocha eterna, sustentando os que nele esperam e guardando os que permanecem sob sua proteção poderosa.""",

    # 12
    """Sede fortes e corajosos; não temais, nem vos assombreis diante das adversidades, pois o Senhor, vosso Deus, é quem vai convosco. Ele não vos deixará nem vos desamparará. Caminhai confiantes, sabendo que Aquele que prometeu é fiel para cumprir tudo o que declarou ao seu povo.""",

    # 13
    """Buscai ao Senhor enquanto se pode achar, invocai-o enquanto está perto. Deixe o ímpio o seu caminho e o homem mau os seus pensamentos. Converta-se ao Senhor, que se compadecerá; volte-se para o nosso Deus, que é rico em perdoar, pois seus pensamentos são mais altos do que os nossos.""",

    # 14
    """Disse Jesus: Eu sou o caminho, a verdade e a vida; ninguém vem ao Pai senão por mim. Se me conhecêsseis, também conheceríeis a meu Pai; e desde agora o conheceis e o tendes visto. Quem me vê a mim vê o Pai, pois Eu e o Pai somos um em essência e propósito.""",

    # 15
    """Tudo posso naquele que me fortalece. Contudo, o Senhor supre todas as minhas necessidades segundo a sua riqueza em glória. Ele me sustenta em meio às dificuldades e me capacita para enfrentar cada desafio, renovando minhas forças e guardando meu coração em perfeita paz.""",

    # 16
    """Bendize, ó minha alma, ao Senhor, e tudo o que há em mim bendiga ao seu santo nome. Não te esqueças de nenhum dos seus benefícios: Ele perdoa as tuas iniquidades, sara as tuas enfermidades, resgata tua vida da perdição e te coroa de graça e misericórdia, renovando-te como águia.""",

    # 17
    """Porque eu bem sei os planos que tenho para vós, diz o Senhor: planos de paz e não de mal, para vos dar um futuro e uma esperança. Então me invocareis, passareis a orar a mim, e Eu vos ouvirei; buscar-me-eis e me achareis quando me buscardes de todo o vosso coração.""",

    # 18
    """A resposta branda desvia o furor, mas a palavra ríspida suscita a ira. A língua dos sábios derrama conhecimento, mas a boca dos tolos espalha insensatez. Os olhos do Senhor estão em todo lugar, contemplando os maus e os bons. O coração alegre aformoseia o rosto, mas a tristeza do coração abate o espírito.""",

    # 19
    """A fé é a certeza das coisas que se esperam, a convicção de fatos que não se veem. Pela fé, entendemos que os mundos foram criados pela palavra de Deus, de modo que o visível veio a existir do invisível. Sem fé é impossível agradar a Deus, pois é necessário que aquele que se aproxima creia que Ele existe e recompensa os que o buscam.""",

    # 20
    """No amor não há medo; ao contrário, o perfeito amor lança fora o medo, porque o medo implica castigo. Aquele que teme não é aperfeiçoado no amor. Nós o amamos porque Ele nos amou primeiro. Se alguém diz: Eu amo a Deus, mas odeia a seu irmão, é mentiroso, pois quem não ama ao seu irmão, a quem vê, não pode amar a Deus, a quem não vê.""",

    # 21
    """O Senhor é a minha luz e a minha salvação; de quem terei medo? O Senhor é a fortaleza da minha vida; a quem temerei? Quando malfeitores avançam contra mim, tropeçam e caem. Ainda que um exército me cerque, não se atemorizará o meu coração, porque o Senhor me acolhe em sua tenda e me firma sobre a rocha.""",

    # 22
    """Aquele que anda em integridade anda seguro, mas o que perverte seus caminhos será conhecido. Melhor é o pobre que caminha com honestidade do que o insensato que fala mentiras. O homem fiel será abundantemente abençoado, mas o que se apressa para enriquecer não ficará sem punição.""",

    # 23
    """O Senhor, teu Deus, está no meio de ti, poderoso para salvar. Ele se deleitará em ti com alegria, renovar-te-á com seu amor e exultará sobre ti com júbilo. Tirará de ti o opróbrio e te fortalecerá, restaurando tua sorte e firmando teus passos em novos caminhos.""",

    # 24
    """Clama a mim, e responder-te-ei, e anunciar-te-ei coisas grandes e ocultas que não sabes. Porque assim diz o Senhor: Eu sou o Deus de toda a carne; acaso haveria algo difícil demais para mim? Eu restauro, transformo e faço novas todas as coisas segundo o conselho da minha vontade.""",

    # 25
    """A sabedoria é superior às joias e nada do que se deseja se compara a ela. Comigo está o conselho, a prudência, a fortaleza e a inteligência. Eu amo os que me amam e os que cedo me buscam me encontram. Riquezas e honra estão comigo; bens duráveis e justiça acompanham meu caminho.""",

    # 26
    """O homem bom alcança o favor do Senhor, mas ao homem de perversidade Ele condena. O preguiçoso deseja e nada consegue, mas o diligente é plenamente suprido. O justo odeia a palavra de mentira; já o ímpio envergonha e desonra a si mesmo.""",

    # 27
    """Aquele que semeia pouco colherá pouco; o que semeia com abundância colherá com abundância. Cada um contribua segundo propôs no coração, não com tristeza ou por necessidade, porque Deus ama quem dá com alegria. Ele é poderoso para fazer abundar toda graça a fim de que, tendo sempre suficiência, abundeis em toda boa obra.""",

    # 28
    """O Senhor firma os passos do homem bom e se agrada do seu caminho. Ainda que caia, não ficará prostrado, pois o Senhor o sustém com a sua mão. Já fui jovem e agora sou velho, mas nunca vi o justo desamparado, nem sua descendência a mendigar o pão.""",

    # 29
    """O Senhor é o meu rochedo, minha fortaleza e libertador; o meu Deus, meu refúgio, em quem confio. Ele me livra dos inimigos, me conduz a lugares altos e amplia os meus caminhos. Em sua força, salto muralhas; pela sua luz, venço as trevas e sigo adiante sem temor.""",

    # 30
    """Quem habita na presença do Altíssimo encontra descanso seguro. Direi do Senhor: Ele é meu refúgio e meu baluarte, meu Deus em quem confio. Ele te guardará de armadilhas e de perigos invisíveis. Sua fidelidade será tua proteção e sua paz guardará teu coração.""",

    # 31
    """Perto está o Senhor dos que têm o coração quebrantado e salva os de espírito oprimido. Muitas são as aflições do justo, mas de todas elas o Senhor o livra. Ele guarda cada um de seus ossos, nenhum deles se quebra, porque sua mão poderosa sustém os que o temem.""",

    # 32
    """A lei do Senhor é perfeita e restaura a alma; o testemunho do Senhor é fiel e dá sabedoria ao simples. Os preceitos do Senhor são retos e alegram o coração. O temor do Senhor é puro e permanece eternamente. Seus juízos são verdadeiros e todos igualmente justos.""",

    # 33
    """Aquele que guarda a sua boca preserva a sua vida, mas quem muito abre os lábios traz ruína sobre si. O preguiçoso deseja e nada alcança, mas o diligente prospera. O justo aborrece a palavra de engano, mas o ímpio se torna motivo de vergonha.""",

    # 34
    """A soberba precede a ruína, e a altivez do espírito precede a queda. Melhor é ser humilde de espírito com os mansos do que repartir o despojo com os soberbos. O sábio teme e se desvia do mal, mas o insensato se ira e confia em si mesmo.""",

    # 35
    """Porque o Senhor dá sabedoria, e da sua boca procedem o conhecimento e o entendimento. Ele reserva sólida sabedoria para os retos e é escudo para os que caminham com integridade, guardando as veredas da justiça e preservando o caminho de seus santos.""",

    # 36
    """Aquele que anda com os sábios será sábio, mas o companheiro dos insensatos sofrerá dano. A desgraça persegue os pecadores, mas os justos são recompensados com o bem. O homem bom deixa herança aos filhos de seus filhos, mas a riqueza do pecador é guardada para o justo.""",

    # 37
    """A ira do homem não produz a justiça de Deus. Portanto, rejeitai toda impureza e recebei com mansidão a palavra implantada, a qual é poderosa para salvar vossas almas. Tornai-vos praticantes da palavra e não apenas ouvintes, enganando-vos a vós mesmos.""",

    # 38
    """A língua tem poder sobre a vida e sobre a morte; os que a usam com sabedoria comerão do seu fruto. Aquele que encontra uma esposa encontra o bem e alcança a benevolência do Senhor. O pobre fala com súplicas, mas o rico responde com dureza.""",

    # 39
    """Não vos canseis de fazer o bem, porque a seu tempo colhereis, se não desfalecermos. Portanto, enquanto tivermos oportunidade, façamos o bem a todos, especialmente aos da família da fé. Deus não se deixa escarnecer; tudo o que o homem semear, isso também colherá.""",

    # 40
    """O Senhor é bom para todos, e as suas misericórdias alcançam todas as suas obras. Todas as tuas criaturas te bendirão e os teus santos te louvarão. Falarão da glória do teu reino e proclamarão o teu poder, para que os homens saibam os feitos poderosos do Senhor.""",

    # 41
    """A glória de Deus é encobrir as coisas, mas a glória dos reis é investigá-las. Os céus, pela sua altura, e a terra, pela sua profundidade, assim como o coração dos reis, são insondáveis. Quem retira a escória da prata encontra um metal purificado; assim também, quando a injustiça é removida, se firma o trono na justiça.""",

    # 42
    """O Senhor dos Exércitos está conosco; o Deus de Jacó é o nosso refúgio. Ainda que a terra se transtorne e os montes se abalem, nós não temeremos, pois há um rio cujas correntes alegram a cidade de Deus. Deus está no meio dela; jamais será abalada, pois Ele a socorre desde sua manhã.""",

    # 43
    """Alegrai-vos sempre no Senhor; outra vez digo: alegrai-vos. Seja a vossa amabilidade conhecida por todos os homens. Não andeis ansiosos por coisa alguma, mas apresentai vossas petições a Deus com oração e súplica, e a paz de Deus guardará vossos corações e mentes.""",

    # 44
    """Semeai para vós segundo a justiça, ceifai segundo a misericórdia e convertei-vos ao Senhor. Porque é tempo de buscar ao Senhor, até que Ele venha e faça chover justiça sobre vós. A misericórdia e a verdade se encontrarão; a justiça e a paz se abraçarão.""",

    # 45
    """O Senhor é a força do seu povo e o refúgio salvador do seu ungido. Salva o teu povo e abençoa a tua herança; apascenta-os e exalta-os para sempre. O Senhor é escudo e proteção, e nele se alegra o coração de todos os que nele confiam.""",

    # 46
    """Melhor é um pouco com justiça do que grandes rendimentos sem retidão. O coração do homem pode fazer planos, mas a resposta certa vem do Senhor. Todas as obras são limpas aos olhos do homem, mas o Senhor pesa o espírito. Entrega ao Senhor as tuas obras e teus planos serão estabelecidos.""",

    # 47
    """Aquele que esconde suas transgressões jamais prosperará, mas o que as confessa e deixa alcançará misericórdia. Feliz é o homem que teme continuamente, mas o que endurece o coração cairá no mal. O justo considera a causa dos necessitados, mas o ímpio não tem entendimento.""",

    # 48
    """O Senhor reina; tremam os povos. Ele está entronizado entre os querubins; abale-se a terra. O Senhor é grande em Sião e exaltado acima de todos os povos. Exaltai ao Senhor, nosso Deus, e prostrai-vos perante o seu santo monte, porque santo é o Senhor, nosso Deus.""",

    # 49
    """Os que semeiam com lágrimas segarão com alegria. Aquele que leva a preciosa semente, andando e chorando, voltará com júbilo trazendo consigo seus feixes. O Senhor restaura a sorte de seu povo e transforma o pranto em dança, enchendo de alegria os corações abatidos.""",

    # 50
    """Ele fortalece o cansado e renova o vigor daquele que não tem forças. Os jovens se cansam e se fatigam, e os moços caem exaustos; mas os que esperam no Senhor renovam as suas forças, sobem com asas como águias, correm e não se cansam, caminham e não se fatigam."""
]

# ============================================================
#  FUNÇÕES AUXILIARES
# ============================================================

def calcular_tempo_limite(num_palavras: int) -> int:
    """
    50 palavras => 5 min, 100 palavras => 10 min (escala linear).
    Retorna em segundos.
    """
    base_minutos = 5.0
    extra_minutos = (num_palavras - 50) * (5.0 / 50.0)  # até +5 min
    total_minutos = base_minutos + extra_minutos
    return int(total_minutos * 60)


def classificar_velocidade(wpm: float) -> str:
    if wpm < 30:
        return "Lento"
    elif wpm < 50:
        return "Médio"
    else:
        return "Rápido"


def calcular_spans_palavras(texto: str):
    """
    Retorna:
      - lista de palavras
      - lista de spans (start, end) em índice de caractere
    """
    palavras = []
    spans = []
    in_word = False
    start = 0
    for i, ch in enumerate(texto):
        if not ch.isspace():
            if not in_word:
                in_word = True
                start = i
        else:
            if in_word:
                in_word = False
                end = i
                palavra = texto[start:end]
                palavras.append(palavra)
                spans.append((start, end))
    if in_word:
        end = len(texto)
        palavra = texto[start:end]
        palavras.append(palavra)
        spans.append((start, end))
    return palavras, spans


def fmt_tempo(segundos: int) -> str:
    mm = segundos // 60
    ss = segundos % 60
    return f"{mm:02d}:{ss:02d}"


# ============================================================
#  APLICATIVO TKINTER
# ============================================================

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BíbliaTyping Pro - Teste de Digitação Bíblica")

        self.texto_alvo = ""
        self.num_palavras_alvo = 0
        self.tempo_limite = 0
        self.start_time = None
        self.running = False
        self.timer_started = False  # inicia ao digitar a primeira letra

        random.seed()

        self._montar_interface()
        self.root.bind("<Escape>", self._on_esc)

    def _montar_interface(self):
        frame_status = tk.Frame(self.root)
        frame_status.pack(fill="x", padx=10, pady=5)

        self.label_tempo = tk.Label(frame_status, text="Tempo: 00:00 / 00:00 (restante 00:00)")
        self.label_tempo.pack(anchor="w")

        self.label_palavras = tk.Label(frame_status, text="Palavras: 0 / 0")
        self.label_palavras.pack(anchor="w")

        self.label_velocidade = tk.Label(frame_status, text="Velocidade: 0.0 WPM (—)")
        self.label_velocidade.pack(anchor="w")

        frame_alvo = tk.LabelFrame(self.root, text="Texto bíblico (base do teste)")
        frame_alvo.pack(fill="both", expand=True, padx=10, pady=5)

        self.text_alvo = tk.Text(frame_alvo, wrap="word", height=8, font=("Consolas", 11))
        self.text_alvo.pack(fill="both", expand=True)
        self.text_alvo.configure(state="disabled")

        frame_digitado = tk.LabelFrame(self.root, text="Seu texto (palavras erradas em vermelho)")
        frame_digitado.pack(fill="both", expand=True, padx=10, pady=5)

        self.text_digitado = tk.Text(frame_digitado, wrap="word", height=8, font=("Consolas", 11))
        self.text_digitado.pack(fill="both", expand=True)
        self.text_digitado.tag_configure("erro", foreground="red")
        self.text_digitado.bind("<KeyRelease>", self._on_key_release)

        self.label_erros = tk.Label(self.root, text="Palavras incorretas: nenhuma até agora.")
        self.label_erros.pack(anchor="w", padx=10)

        frame_botoes = tk.Frame(self.root)
        frame_botoes.pack(fill="x", padx=10, pady=10)

        self.btn_iniciar = tk.Button(frame_botoes, text="Iniciar novo teste", command=self.iniciar_teste)
        self.btn_iniciar.pack(side="left", padx=5)

        self.btn_finalizar = tk.Button(frame_botoes, text="Finalizar teste", command=self.finalizar_teste)
        self.btn_finalizar.pack(side="left", padx=5)

        # NOVO BOTÃO SOBRE
        self.btn_sobre = tk.Button(frame_botoes, text="Sobre", command=self.mostrar_sobre)
        self.btn_sobre.pack(side="left", padx=5)

        self.btn_sair = tk.Button(frame_botoes, text="Sair", command=self.root.destroy)
        self.btn_sair.pack(side="right", padx=5)

    # =========================
    #   Lógica do teste
    # =========================

    def iniciar_teste(self):
        if self.running:
            return

        self.texto_alvo = random.choice(TEXT_POOL)
        self.num_palavras_alvo = len(self.texto_alvo.split())
        self.tempo_limite = calcular_tempo_limite(self.num_palavras_alvo)

        self.text_alvo.configure(state="normal")
        self.text_alvo.delete("1.0", "end")
        self.text_alvo.insert("1.0", self.texto_alvo)
        self.text_alvo.configure(state="disabled")

        self.text_digitado.configure(state="normal")
        self.text_digitado.delete("1.0", "end")

        self.label_tempo.config(
            text=f"Tempo: 00:00 / {fmt_tempo(self.tempo_limite)} (restante {fmt_tempo(self.tempo_limite)})"
        )
        self.label_palavras.config(text=f"Palavras: 0 / {self.num_palavras_alvo}")
        self.label_velocidade.config(text="Velocidade: 0.0 WPM (—)")
        self.label_erros.config(text="Palavras incorretas: nenhuma até agora.")

        # Timer só começa na primeira tecla
        self.start_time = None
        self.timer_started = False
        self.running = True

        self.text_digitado.focus_set()
        self._update_loop()

    def finalizar_teste(self, auto=False):
        if not self.running:
            return

        self.running = False
        self.timer_started = False

        if self.start_time is None:
            decorrido = 0.0
        else:
            decorrido = time.time() - self.start_time

        texto_dig = self.text_digitado.get("1.0", "end-1c")
        palavras_dig, _ = calcular_spans_palavras(texto_dig)
        palavras_digitadas = len(palavras_dig)

        minutos = max(decorrido / 60.0, 1e-6)
        wpm = palavras_digitadas / minutos
        classificacao = classificar_velocidade(wpm)

        alvo_pal = self.texto_alvo.split()
        palavras_erradas = []
        for i, palavra in enumerate(palavras_dig):
            if i >= len(alvo_pal) or palavra != alvo_pal[i]:
                palavras_erradas.append(palavra)

        msg = (
            f"Tempo total: {fmt_tempo(int(decorrido))}\n"
            f"Palavras digitadas: {palavras_digitadas}\n"
            f"Velocidade média: {wpm:.1f} WPM\n"
            f"Classificação: {classificacao}\n\n"
        )
        if palavras_erradas:
            msg += "Palavras incorretas:\n" + ", ".join(palavras_erradas)
        else:
            msg += "Nenhuma palavra incorreta (texto igual ao alvo)."

        titulo = "Resultado final" if not auto else "Tempo esgotado — Resultado"
        messagebox.showinfo(titulo, msg)

        self.text_digitado.configure(state="disabled")

    def _update_loop(self):
        if not self.running:
            return

        agora = time.time()
        if self.timer_started and self.start_time is not None:
            decorrido = agora - self.start_time
        else:
            decorrido = 0.0

        if self.timer_started and decorrido >= self.tempo_limite:
            self.finalizar_teste(auto=True)
            return

        restante = self.tempo_limite - int(decorrido) if self.timer_started else self.tempo_limite

        texto_dig = self.text_digitado.get("1.0", "end-1c")
        palavras_dig, spans = calcular_spans_palavras(texto_dig)
        palavras_digitadas = len(palavras_dig)

        minutos = max(decorrido / 60.0, 1e-6)
        wpm = palavras_digitadas / minutos if self.timer_started else 0.0
        classificacao = classificar_velocidade(wpm) if self.timer_started else "—"

        self.label_tempo.config(
            text=f"Tempo: {fmt_tempo(int(decorrido))} / {fmt_tempo(self.tempo_limite)} "
                 f"(restante {fmt_tempo(restante)})"
        )
        self.label_palavras.config(
            text=f"Palavras: {palavras_digitadas} / {self.num_palavras_alvo}"
        )
        self.label_velocidade.config(
            text=f"Velocidade: {wpm:.1f} WPM ({classificacao})"
        )

        all_correct = self._atualizar_erros_e_checar_completo(palavras_dig, spans)

        if self.timer_started and all_correct and palavras_digitadas > 0:
            self.finalizar_teste(auto=False)
            return

        self.root.after(200, self._update_loop)

    def _atualizar_erros_e_checar_completo(self, palavras_dig, spans):
        self.text_digitado.tag_remove("erro", "1.0", "end")

        alvo_pal = self.texto_alvo.split()
        palavras_erradas = []
        all_correct = True

        for i, palavra in enumerate(palavras_dig):
            if i >= len(alvo_pal) or palavra != alvo_pal[i]:
                palavras_erradas.append(palavra)
                all_correct = False
                start_char, end_char = spans[i]
                idx_ini = f"1.0+{start_char}c"
                idx_fim = f"1.0+{end_char}c"
                self.text_digitado.tag_add("erro", idx_ini, idx_fim)

        if len(palavras_dig) != len(alvo_pal):
            all_correct = False

        if palavras_erradas:
            erros_str = ", ".join(palavras_erradas)
            if len(erros_str) > 120:
                erros_str = erros_str[:117] + "..."
            self.label_erros.config(text=f"Palavras incorretas: {erros_str}")
        else:
            self.label_erros.config(text="Palavras incorretas: nenhuma até agora.")

        return all_correct

    def _on_key_release(self, event):
        if self.running and not self.timer_started:
            texto = self.text_digitado.get("1.0", "end-1c")
            if texto.strip():
                self.start_time = time.time()
                self.timer_started = True

    def _on_esc(self, event):
        if self.running:
            self.finalizar_teste(auto=False)

    def mostrar_sobre(self):
        messagebox.showinfo(
            "Sobre - BíbliaTyping Pro",
            "BíbliaTyping Pro - Teste de Velocidade de Digitação Bíblica\n\n"
            "Desenvolvedor: Caio Monteiro\n"
            "Versão: 1.0 - 12/2025\n\n"
            "Leopoldina - MG\n"
            "Github: @chacalbl4ck\n"
            "\n"
            "DEUS SEJA LOUVADO!\n"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
