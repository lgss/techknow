const newTab = (string) => {
    return string.replace(`<a href`, `<a target="_blank" href`);
};
export default newTab;
