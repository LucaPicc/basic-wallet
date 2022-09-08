import '../../styles/buttons.css';

const Button = ({label, invert, onClick}) => {
    return (
        <button
            onClick={onClick}
            className='base_button'
            type='submit'
        >
            {label}
        </button>
    )
};

export default Button

