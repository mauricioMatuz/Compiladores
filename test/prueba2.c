char line[100];/* line of data from the input */int result;char operator; /* operator the user specified */int value;/* the result of the calculations */int main(){result = 0; /* si inicia el resultado */while (1){printf("Result: %d\n", result);printf("Enter operator and number: ");fgets(line, sizeof(line), stdin);sscanf(line, "%c %d", operator, value);printf("## despues del scanf %c\n", operator);if (operator == '+') {printf("## despues del if %c\n", operator);result += value;} else {printf("Unknown operator %c\n", operator);}}}