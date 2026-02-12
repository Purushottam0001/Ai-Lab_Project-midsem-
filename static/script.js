function addRow() {
    let div = document.createElement("div");
    div.className = "row";

    div.innerHTML = `
        <input type="text" name="subject" placeholder="Subject" required>
        <input type="number" name="hours" placeholder="Study Hours" required>
        <select name="difficulty">
            <option>Easy</option>
            <option>Medium</option>
            <option>Hard</option>
        </select>
    `;

    document.getElementById("subjects").appendChild(div);
}
