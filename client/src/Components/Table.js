export default function Table({ heading, body, caption }) {
    return (
        <table>
            {caption.map(c => <caption> {c} </caption>)}
            <thead>
                <tr>
                    {heading.map(heading => {
                        return <th key={heading}>{heading}</th>
                    })}
                </tr>
            </thead>
            <tbody>
                {body.map((row, index) =>
                    <tr key={index}>
                        {row.map((val, index) => <td key={index}>{val}</td>)}
                    </tr>
                )}
            </tbody>
        </table>
    );
}
