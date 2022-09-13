import 'styles/basic-card.css';

const BasicCard = ({children, style}) => {
    return(
        <div 
            className="basic_card__container"
            style={style}
            >
            {children}
        </div>
    )
}

export default BasicCard;
