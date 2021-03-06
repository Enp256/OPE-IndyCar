from django import forms
from funilaria.models import Cliente,Empresa,Orcamento,OrdemDeServico,Customer,Material,Estado,Carrinho
from funilaria.views import *
from .widgets import FengyuanChenDatePickerInput
from .validacao import *
from .fields import DataField


class CustomerForm(forms.ModelForm):
    
    nome = forms.CharField(max_length=60,label='Nome completo:', widget = forms.TextInput(attrs={
        'placeholder':'Informe o nome',
        'name':'nome',
        'class':'inputText',
        'id':'nome',
        'onkeyup':'validarNome()',
        'autocomplete': 'off'}))
    endereco = forms.CharField(max_length=100,label='Endereço:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o endereço',
        'name':'endereco',
        'class':'inputText',
        'id':'endereco',
        'onkeyup':'validarEndereco()',
        'autocomplete': 'off'}))
    bairro = forms.CharField(max_length=30,label='Bairro:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o bairro',
        'name':'bairro',
        'class':'inputText',
        'id':'bairro',
        'onkeyup':'validarBairro()',
        'autocomplete': 'off'}))
    email = forms.EmailField(max_length=60,label='Email:',widget = forms.EmailInput(attrs={
        'placeholder':'Informe o email',
        'name':'email',
        'class':'inputText',
        'id':'email',
        'onkeyup':'validarEmail()',
        'autocomplete': 'off'}))
    telefone = forms.CharField(max_length=16,label='Telefone:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o telefone',
        'name':'tel',
        'class':'inputText', #'tele'
        'id':'tel',
        'onkeyup':'validarTelefone()',
        'autocomplete': 'off'}))

    def validar(self):
        dados=self.cleaned_data
        nome=dados.get('nome')
        endereco=dados.get('endereco')
        bairro=dados.get('bairro')
        email=dados.get('email')
        telefone=dados.get('telefone')
        

        if not somenteLetras(nome):
            raise forms.ValidationError('Nome inválido !')

        if not somenteLetras(bairro):
            raise forms.ValidationError('Bairro inválido !')

        if not validarTelefone(telefone):
            raise forms.ValidationError('Telefone inválido !')

    class Meta:
        abstract=True



class ClienteForm(CustomerForm):
    cpf = forms.CharField(error_messages={'unique':"This email has already been registered."},max_length=14, min_length=11, label='CPF:', widget = forms.TextInput(attrs={
        'placeholder':'Informe o CPF',
        'name':'cpf',
        'class':'inputText',
        'id':'cpf',
        'onkeyup':'validarCPF()',
        'autocomplete': 'off'}))

    def clean(self):
        dados = self.cleaned_data
        cpf=dados.get('cpf')
        #or not validarTamanho(cpf,11) 
        if not somenteNumeros(cpf) or not validarCpf2(cpf):
            raise forms.ValidationError('CPF inválido !')
        self.validar()

    class Meta:
        model = Cliente
        fields=['cpf','nome','endereco','bairro','email','telefone']

    

class EmpresaForm(CustomerForm):
    cnpj = forms.CharField(error_messages={'unique':"This email has already been registered."},min_length=14, max_length=18,label='CNPJ:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o CNPJ',
        'name':'cnpj',
        'class':'inputText',
        'id':'cnpj',
        'onkeyup':'validarCNPJ()',
        'autocomplete': 'off'}))

    def clean(self):
        dados = self.cleaned_data
        cnpj=dados.get('cnpj')
        if not somenteNumeros(cnpj)  or not validarCnpj(cnpj):
            raise forms.ValidationError('CNPJ inválido !')
        self.validar()

    class Meta:
        model = Empresa
        fields=['cnpj','nome','endereco','bairro','email','telefone']

class OrdemDeServicoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(empty_label=" Selecione",queryset=Customer.objects.all().select_subclasses(Cliente,Empresa),widget=forms.Select(attrs={'class':'inputText'}))#.order_by('id'))
    marca_veiculo = forms.CharField(max_length=30,label='Marca:',widget = forms.TextInput(attrs={
        'placeholder':'Informe a marca',
        'name':'marca',
        'class':'inputText',
        'id':'marca',
        'onkeyup':'validarMarca()',
        'autocomplete': 'off'}))
    modelo_veiculo = forms.CharField(max_length=30,label='Modelo:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o modelo',
        'name':'modelo',
        'class':'inputText',
        'id':'modelo',
        'onkeyup':'validarModelo()',
        'autocomplete': 'off'}))
    cor_veiculo = forms.CharField(max_length=30,label='Cor:',widget = forms.TextInput(attrs={
        'placeholder':'Informe a cor',
        'name':'cor',
        'class':'inputText',
        'id':'cor',
        'onkeyup':'validarCor()',
        'autocomplete': 'off'}))
    placa_veiculo = forms.CharField(max_length=8,label='Placa:',widget = forms.TextInput(attrs={
        'placeholder':'',
        'name':'placa',
        'class':'inputLittle',
        'id':'placa',
        'onkeyup':'validarPlaca()',
        'autocomplete': 'off'}))
    ano_veiculo = forms.CharField(max_length=4,label='Ano:',widget = forms.NumberInput(attrs={
        'placeholder':'',
        'name':'ano',
        'class':'inputLittle',
        'id':'ano',
        'onkeyup':'validarAno()',
        'autocomplete': 'off'}))
    estado_veiculo= forms.ModelChoiceField(empty_label=" Selecione",queryset=Estado.objects.all(),widget=forms.Select(attrs={'class':'estado'}))
    cidade_veiculo = forms.CharField(max_length=30,label='Cidade:',widget = forms.TextInput(attrs={
        'placeholder':'Informe a cidade',
        'name':'cidade',
        'class':'inputText',
        'id':'cidade',
        'onkeyup':'validarCidade()',
        'autocomplete': 'off'}))
    reparos_necessarios = forms.CharField(max_length=500,label='Reparos necessários:',widget = forms.Textarea(attrs={
        'placeholder':'Informe os reparos necessários',
        'name':'reparos_necessarios',
        'class':'inputReparo',
        'id':'inputReparo',
        'onkeyup':'validarReparoOS()',
        'autocomplete': 'off'}))
    prazo_entrega = forms.DateField(label='Prazo entrega:',input_formats=['%d/%m/%Y'],widget = FengyuanChenDatePickerInput(attrs={
        'placeholder':'Prazo de entrega',
        'name':'prazo_entrega',
        'class':"date",
        'id':'prazo_entrega',
        'onkeyup':'validarPrazoEntrega()',
        'autocomplete': 'off'}))
    data_finalizacao = DataField(required=False,label='Data de finalização:',input_formats=['%d/%m/%Y'],widget = FengyuanChenDatePickerInput(attrs={
        'placeholder':'Data de finalização',
        'name':'data_finalizacao',
        'class':"date",
        'id':'data_finalizacao',
        'autocomplete': 'off'}))
    
    def clean(self):
        dados=self.cleaned_data
        reparos_necessarios=dados.get('reparos_necessarios')
        entrada=dados.get('entrada')
        data_finalizacao=dados.get('data_finalizacao')
        prazo_entrega=dados.get('prazo_entrega')
        finalizado=dados.get('finalizado')
        marca_veiculo=dados.get('marca_veiculo')
        modelo_veiculo=dados.get('modelo_veiculo')
        cor_veiculo=dados.get('cor_veiculo')
        placa_veiculo=dados.get('placa_veiculo')
        ano_veiculo=dados.get('ano_veiculo')
        cidade_veiculo=dados.get('cidade_veiculo')
        estado_veiculo=dados.get('estado_veiculo')

        '''if not somenteLetras(reparos_necessarios):
            raise forms.ValidationError('Reparos necessários inválidos !')'''

        if not somenteLetras(marca_veiculo):
            raise forms.ValidationError('Marca inválida !')

        if not validarModelo(modelo_veiculo):
            raise forms.ValidationError('Modelo inválido !')

        if not somenteLetras(cor_veiculo):
            raise forms.ValidationError('Cor inválida !')

        if not validarPlaca(placa_veiculo):
            raise forms.ValidationError('Placa inválida !')

        if not validarAno(ano_veiculo):
            raise forms.ValidationError('Ano inválido !')

        if not somenteLetras(cidade_veiculo):
            raise forms.ValidationError('Cidade inválida !')

        if type(estado_veiculo)!=Estado:
            raise forms.ValidationError('Estado inválido !')

        if not validarDataObrigatoria(prazo_entrega):
            raise forms.ValidationError('Prazo inválido !')
        
        if not validarData(data_finalizacao):
            raise forms.ValidationError('Data de finalização inválida !')

    class Meta:
        model = OrdemDeServico
        fields=['cliente','marca_veiculo','modelo_veiculo','cor_veiculo','placa_veiculo','ano_veiculo','estado_veiculo','cidade_veiculo','reparos_necessarios','prazo_entrega','data_finalizacao']

class MaterialForm(forms.ModelForm):
    quantidade_estoque = forms.CharField(max_length=6,label='Quantidade em estoque:',widget = forms.NumberInput(attrs={
        'placeholder':'Informe a quantidade em estoque',
        'class':'inputMaterial',
        #'name':'quantidade_estoque',
        'id':'quantidade_estoque',
        'onkeyup':'validarQTDestoque()',
        'autocomplete': 'off'}))
    descricao = forms.CharField(max_length=200,label='Descrição:',widget = forms.TextInput(attrs={
        'placeholder':'Informe a descrição',
        'class':'inputMaterial',
        #'name':'descricao',
        'id':'descricao',
        'onkeyup':'validarDescricao()',
        'autocomplete': 'off'}))
    
    valor = forms.CharField(max_length=9,label='Valor:',widget = forms.TextInput(attrs={
        'placeholder':'Valor da peça',
        'name':'valor',
        'class':'inputMaterial',
        'class':'money',
        'id':'valor',
        'onkeyup':'validarValor()',
        'autocomplete': 'off'}))
    
    def clean(self):
        dados=self.cleaned_data
        quantidade_estoque=dados.get('quantidade_estoque')
        descricao=dados.get('descricao')
        valor=dados.get('valor')

        '''if not somenteLetras(descricao):
            raise forms.ValidationError('Descricao inválida !')'''

        if not somenteNumeros(valor):
            raise forms.ValidationError('Valor inválido !')

        if not validarQtd(quantidade_estoque):
            raise forms.ValidationError('Quantidade inválida !')
        
    
    class Meta:
        model = Material
        fields=['quantidade_estoque','descricao','valor']

class OrcamentoForm(forms.ModelForm):
    ordem_de_servico = forms.ModelChoiceField(queryset=OrdemDeServico.objects.all(),widget=forms.Select(attrs={'class':'inputText'}))
    servicos = forms.CharField(max_length=500,label='Serviços:',widget = forms.Textarea(attrs={
        'placeholder':'Informe os serviços necessários',
        'name':'servicos',
        'class':'inputServico',
        'onkeyup':'validarServicos()',
        'id':'servicos'}))
    carrinho = forms.ModelChoiceField(queryset=Carrinho.objects.all().order_by('id'),widget=forms.HiddenInput())
    valor_mao_de_obra = forms.DecimalField(label='Valor da mão de obra:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o valor',
        'name':'valor_mao_de_obra',
        'class':'inputText',
        'class':'money',
        'id':'valor_mao_de_obra',
        'autocomplete': 'off',
        'onkeyup':'calcularTotal()'}))
    previsao_entrega = forms.DateField(label='Previsão entrega:',input_formats=['%d/%m/%Y'],widget = FengyuanChenDatePickerInput(attrs={
        'placeholder':'Previsão de entrega',
        'name':'previsao_entrega',
        'class':"date",
        'id':'previsao_entrega',
        'autocomplete': 'off'}))
    data_saida = forms.DateField(required=False,label='Data saída:',input_formats=['%d/%m/%Y'],widget = FengyuanChenDatePickerInput(attrs={
        'placeholder':'Data de saída',
        'name':'data_saida',
        'class':"date",
        'id':'data_saida',
        'autocomplete': 'off'}))
    
    def clean(self):
        dados=self.cleaned_data
        ordem_de_servico=dados.get('ordem_de_servico')
        servicos=dados.get('servicos')
        valor_mao_de_obra=dados.get('valor_mao_de_obra')
        previsao_entrega=dados.get('previsao_entrega')
        data_saida=dados.get('data_saida')
        carrinho=dados.get('carrinho')


        """if not somenteLetras(servicos):
            raise forms.ValidationError('Serviços inválidos !')"""

        """ if not somenteNumeros(valor_mao_de_obra):
            raise forms.ValidationError('Valor mão de obra inválido !') """

        """ if not somenteNumeros(total_a_pagar):
            raise forms.ValidationError('Total a pagar inválido !') """
    
        if not validarData(previsao_entrega):
            raise forms.ValidationError('Data de previsao_entrega inválida !')

        if not validarData(data_saida):
            raise forms.ValidationError('Data de data_saida inválida !')         

    class Meta:
        model = Orcamento
        fields=['ordem_de_servico','carrinho','servicos','valor_mao_de_obra','previsao_entrega','data_saida']       


class LucrosForm(forms.Form):
    data_inicial = forms.DateField(required=False,label='Data inicial:',input_formats=['%d/%m/%Y'],widget = FengyuanChenDatePickerInput(attrs={
        'placeholder':'Data inicial',
        'name':'data_inicial',
        'class':"date",
        'id':'data_inicial',
        'autocomplete': 'off'}))
    data_final = forms.DateField(required=False,label='Data final   ',input_formats=['%d/%m/%Y'],widget = FengyuanChenDatePickerInput(attrs={
        'placeholder':'Data final',
        'name':'data_final',
        'class':"date",
        'id':'data_final',
        'autocomplete': 'off'}))
