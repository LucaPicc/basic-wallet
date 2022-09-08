import 'styles/text-input.css'

const TextInput = ({onChange, label, type, props}) => {
    return (
        <div className='input_container'>
            <label className='input_label'>{label}</label>
            <input {...props} className='input_elem' type={type}/>
        </div>
    )
}

export default TextInput