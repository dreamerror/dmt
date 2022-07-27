#pragma once

class Productivity {
    private:
        int qualification;
        int count;
        double motivation;
        double productivity;

        void calc_motivation() {
            motivation = 1;
            if (qualification <= 5 && count >= 3) {
                motivation /= 2;
            }
        }

        void calc_productivity() {
            productivity = 1;
            if (qualification < 10) {
                productivity /= (10 - qualification);
            }
            if (count < 3) {
                productivity /= 2;
            } else if (count > 4) {
                productivity /= 3;
            }
            productivity *= motivation;
        }

        void update_productivity() {
            calc_motivation();
            calc_productivity();
        }

    public:
        Productivity() {
            qualification = 10;
            count = 3;
            motivation = 1;
            productivity = 1;
        }

        int get_qualification() {
            return qualification;
        }

        void set_qualification(int qualification_) {
            qualification = qualification_;
            update_productivity();
        }

        int get_count() {
            return count;
        }

        void set_count(int count_) {
            count = count_;
            update_productivity();
        }

        double get_motivation() {
            return motivation;
        }

        double get_productivity() {
            return productivity;
        }

};
