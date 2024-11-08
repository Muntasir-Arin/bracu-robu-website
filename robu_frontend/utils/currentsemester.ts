export function getCurrentSemester(): string {
    const currentDate: Date = new Date();
    const currentMonth: number = currentDate.getMonth(); // Month is zero-indexed (0 = January, 11 = December)
    const currentYear: number = currentDate.getFullYear();

    let semester: string = "";
    let year: number = currentYear;

    if (currentMonth >= 0 && currentMonth <= 4) {
        semester = "Spring";
    } else if (currentMonth >= 5 && currentMonth <= 7) {
        semester = "Summer";
    } else {
        semester = "Fall";
    }

    return `${semester} ${year}`;
}
