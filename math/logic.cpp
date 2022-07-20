#include "logic.h"

double get_motivation(int qualification, int count) {
    double motivation = 1;
    if (qualification <= 5 && count >= 3) {
        motivation /= 2;
    }
    return motivation;
}

double get_productivity(int qualification, int count) {
    double productivity = 1;
    productivity /= (10 - qualification);
    if (count < 3) {
        productivity /= 2;
    } else if (count > 4) {
        productivity /= 3;
    }
    productivity *= get_motivation(qualification, count);
    return productivity;
}
