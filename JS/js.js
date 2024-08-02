// Função para adicionar dois números
function add(num1, num2) {
    return num1 + num2;
}

// Função para subtrair dois números
function subtract(num1, num2) {
    return num1 - num2;
}

// Função para multiplicar dois números
function multiply(num1, num2) {
    return num1 * num2;
}

// Função para dividir dois números
function divide(num1, num2) {
    if (num2 === 0) {
        return 'Erro: divisão por zero';
    }
    return num1 / num2;
}

// Exemplo de uso das funções
const number1 = 10;
const number2 = 5;

const additionResult = add(number1, number2);
console.log(`Adição: ${additionResult}`);

const subtractionResult = subtract(number1, number2);
console.log(`Subtração: ${subtractionResult}`);

const multiplicationResult = multiply(number1, number2);
console.log(`Multiplicação: ${multiplicationResult}`);

const divisionResult = divide(number1, number2);
console.log(`Divisão: ${divisionResult}`);
