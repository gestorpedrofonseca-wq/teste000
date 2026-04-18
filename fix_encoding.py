import os

def check_and_fix(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        
        if 'Ã§' in text or 'Ã£' in text or 'Ã¡' in text or 'Ã©' in text or 'Ãª' in text or 'Ã' in text:
            print(f"Found Mojibake in {filename}")
            try:
                # Attempt to recover original bytes
                original_bytes = text.encode('cp1252')
                # Check if these bytes form valid utf-8
                original_bytes.decode('utf-8')
                
                with open(filename, 'wb') as f:
                    f.write(original_bytes)
                print(f"Fixed {filename} successfully via cp1252 encode.")
            except UnicodeError:
                # Fallback to string replacement for common Portuguese Mojibake
                print(f"Fallback to string replace for {filename}")
                replacements = {
                    'Ã¡': 'á', 'Ã ': 'à', 'Ã¢': 'â', 'Ã£': 'ã', 'Ã¤': 'ä',
                    'Ã©': 'é', 'Ã¨': 'è', 'Ãª': 'ê', 'Ã«': 'ë',
                    'Ã­': 'í', 'Ã¬': 'ì', 'Ã®': 'î', 'Ã¯': 'ï',
                    'Ã³': 'ó', 'Ã²': 'ò', 'Ã´': 'ô', 'Ãµ': 'õ', 'Ã¶': 'ö',
                    'Ãº': 'ú', 'Ã¹': 'ù', 'Ã»': 'û', 'Ã¼': 'ü',
                    'Ã§': 'ç', 'Ã±': 'ñ',
                    'Ã': 'Á', 'Ã€': 'À', 'Ã¢': 'Â', 'Ãƒ': 'Ã', 'Ã„': 'Ä',
                    'Ã‰': 'É', 'Ãˆ': 'È', 'ÃŠ': 'Ê', 'Ã‹': 'Ë',
                    'Ã': 'Í', 'ÃŒ': 'Ì', 'ÃŽ': 'Î', 'Ã': 'Ï',
                    'Ã“': 'Ó', 'Ã’': 'Ò', 'Ã”': 'Ô', 'Ã•': 'Õ', 'Ã–': 'Ö',
                    'Ãš': 'Ú', 'Ã™': 'Ù', 'Ã›': 'Û', 'Ãœ': 'Ü',
                    'Ã‡': 'Ç', 'Ã‘': 'Ñ',
                    'Ajudando CrianÃ§as e FamÃ­lias no Tocante Ã  Garantia': 'Ajudando Crianças e Famílias no Tocante à Garantia',
                    'DoaÃ§Ã£o': 'Doação',
                    'TransparÃªncia': 'Transparência',
                    'NÃ£o': 'Não',
                    'fÃªnix': 'fênix',
                    'FÃŠNIX': 'FÊNIX',
                    'crianÃ§as': 'crianças',
                    'famÃ­lias': 'famílias',
                    'EducaÃ§Ã£o': 'Educação',
                    'AÃ§Ã£o': 'Ação',
                    'aÃ§Ãµes': 'ações',
                    'AÃ§Ãµes': 'Ações',
                    'InstituiÃ§Ã£o': 'Instituição',
                    'instituiÃ§Ãµes': 'instituições',
                    'sÃ£o': 'são',
                    'SÃ£o': 'São',
                    'SaÃºde': 'Saúde',
                    'PÃºblica': 'Pública',
                    'atravÃ©s': 'através',
                    'vocÃª': 'você',
                    'VocÃª': 'Você',
                    'JÃ¡': 'Já',
                    'jÃ¡': 'já',
                    'AladÃª': 'Aladê',
                    'ItapuÃ£': 'Itapuã',
                    'mÃªs': 'mês',
                    'bancÃ¡rio': 'bancário',
                    'BancÃ¡rio': 'Bancário',
                    'AgÃªncia': 'Agência',
                    'Conta': 'Conta',
                    'depÃ³sito': 'depósito',
                    'DepÃ³sito': 'Depósito',
                    'DoaÃ§Ãµes': 'Doações',
                    'doaÃ§Ãµes': 'doações',
                    'Projetos': 'Projetos',
                    'Contato': 'Contato',
                    'O Instituto': 'O Instituto',
                    'Causas': 'Causas',
                    'concluiÃ­do': 'concluído',
                    'TÃ­tulo': 'Título',
                    'descriÃ§Ã£o': 'descrição'
                }
                
                for k, v in replacements.items():
                    text = text.replace(k, v)
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f"Fixed {filename} via string replacement.")
    except Exception as e:
        print(f"Error with {filename}: {e}")

for f in os.listdir('.'):
    if f.endswith('.html'):
        check_and_fix(f)
