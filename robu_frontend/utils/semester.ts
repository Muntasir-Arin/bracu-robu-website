// TODO: Need to make it proper
function getSemester(): string {
  const date = new Date();
  const month = date.getMonth();
  const year = date.getFullYear();

  if (month >= 11 && month <= 1) {
    return `Fall ${year}`;
  } else if (month >= 2 && month <= 4) {
    return `Spring ${year}`;
  } else {
    return `Summer ${year}`;
  }
}

export { getSemester };
