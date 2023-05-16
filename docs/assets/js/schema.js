function toggle(event) {
    const id = event.currentTarget.id;

    const subBlock = document.getElementById(`sub_${id}`);
    subBlock.classList.toggle('hidden');

    const arrow = document.querySelector(`#${id} .arrow`);
    arrow.classList.toggle('arrow-open');
}
