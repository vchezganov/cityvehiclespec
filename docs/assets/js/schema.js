function toggle(event) {
    let id = event.currentTarget.id;

    const subBlock = document.getElementById(`sub_${id}`);
    const display = window.getComputedStyle(subBlock).display;
    const isHidden = display === 'none';

    subBlock.style.display = isHidden ? 'block' : 'none';
}
