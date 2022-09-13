import 'styles/buttons.css';

const Button = ({label, invert, onClick, props}) => {
    return (
        <button
            onClick={onClick}
            className='base_button'
            {...props}
        >
            {label}
        </button>
    )
};

export default Button

