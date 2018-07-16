import gql from 'graphql-tag'

export const RegisterGQL = gql`
    mutation( $username: String! , $password: String! , $email: String! , $displayname: String! , $school: String , $company: String , $location: String ){
        Register(username: $username , password: $password , email: $email , displayname: $displayname, school: $school , company: $company , location: $location ){
            token
            payload
        }
    }
`
