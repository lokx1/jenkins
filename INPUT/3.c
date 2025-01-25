#include "stdio.h"
int divide(int a, int b) {
    return b != 0 ? a / b : 0; // Return 0 if division by zero
}